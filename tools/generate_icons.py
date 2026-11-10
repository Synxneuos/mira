import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from collections import deque

def main():
    src = r'c:\Users\Naquib\Downloads\mira\images\mira_concept_4_cozy_sprite.jpg'
    im = Image.open(src).convert('RGB')
    w_orig, h_orig = im.size

    # Save brand assets
    os.makedirs('images/brand', exist_ok=True)
    head_im = im.resize((1254, 1254), Image.Resampling.LANCZOS)
    head_im.save('images/brand/mira-head.png', 'PNG')
    head_im.save('images/brand/mira-head.png', 'PNG')
    
    avatar_im = im.resize((512, 512), Image.Resampling.LANCZOS)
    avatar_im.save('images/avatar-org.png', 'PNG')
    os.makedirs('desktop/icon', exist_ok=True)
    avatar_im.save('desktop/icon/Mira.icns')
    avatar_im.save('desktop/icon/Mira.icns')
    print("Saved brand, avatar, and desktop icon assets")

    # Extract transparent foreground
    arr = np.array(im)
    h, w, _ = arr.shape
    is_bg = np.zeros((h, w), dtype=bool)

    diff = np.max(255 - arr, axis=2)
    near_white = (diff < 24)

    queue = deque()
    for x in range(w):
        if near_white[0, x]: queue.append((0, x)); is_bg[0, x] = True
        if near_white[h-1, x]: queue.append((h-1, x)); is_bg[h-1, x] = True
    for y in range(h):
        if near_white[y, 0]: queue.append((y, 0)); is_bg[y, 0] = True
        if near_white[y, w-1]: queue.append((y, w-1)); is_bg[y, w-1] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not is_bg[ny, nx] and near_white[ny, nx]:
                    is_bg[ny, nx] = True
                    queue.append((ny, nx))

    alpha = np.where(is_bg, 0, 255).astype(np.uint8)
    alpha_img = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(radius=1.2))
    
    rgba = Image.new('RGBA', (w, h))
    rgba.paste(im, (0, 0))
    rgba.putalpha(alpha_img)

    # Crop to content
    bbox = rgba.getbbox()
    cropped = rgba.crop(bbox)

    densities = {
        'mdpi': (48, 108),
        'hdpi': (72, 162),
        'xhdpi': (96, 216),
        'xxhdpi': (144, 324),
        'xxxhdpi': (192, 432),
    }

    for dens, (icon_size, fg_size) in densities.items():
        folder = os.path.join('app', 'src', 'main', 'res', f'mipmap-{dens}')
        os.makedirs(folder, exist_ok=True)

        # 1. Background
        bg = Image.new('RGB', (fg_size, fg_size), (255, 255, 255))
        bg.save(os.path.join(folder, 'ic_launcher_background.webp'), 'WEBP', quality=100)

        # 2. Foreground (adaptive target size: ~60% of fg_size)
        fg = Image.new('RGBA', (fg_size, fg_size), (0, 0, 0, 0))
        target_char_size = int(fg_size * 0.62)
        # Preserve aspect ratio
        aspect = cropped.width / cropped.height
        if aspect >= 1:
            cw = target_char_size
            ch = int(cw / aspect)
        else:
            ch = target_char_size
            cw = int(ch * aspect)
        scaled_char = cropped.resize((cw, ch), Image.Resampling.LANCZOS)
        offset_x = (fg_size - cw) // 2
        offset_y = (fg_size - ch) // 2
        fg.paste(scaled_char, (offset_x, offset_y), scaled_char)
        fg.save(os.path.join(folder, 'ic_launcher_foreground.webp'), 'WEBP', quality=100)

        # 3. Monochrome
        mono = Image.new('RGBA', (fg_size, fg_size), (0, 0, 0, 0))
        # Use alpha of fg
        fg_arr = np.array(fg)
        mono_arr = np.zeros_like(fg_arr)
        mono_arr[:, :, 3] = fg_arr[:, :, 3]
        # Dark silhouette
        mono_arr[:, :, 0] = 30
        mono_arr[:, :, 1] = 30
        mono_arr[:, :, 2] = 30
        mono = Image.fromarray(mono_arr, 'RGBA')
        mono.save(os.path.join(folder, 'ic_launcher_monochrome.webp'), 'WEBP', quality=100)

        # 4. Standard launcher icon
        # Composite scaled character directly onto white square icon
        icon = Image.new('RGB', (icon_size, icon_size), (255, 255, 255))
        char_icon_size = int(icon_size * 0.88)
        if aspect >= 1:
            icw = char_icon_size
            ich = int(icw / aspect)
        else:
            ich = char_icon_size
            icw = int(ich * aspect)
        scaled_icon_char = cropped.resize((icw, ich), Image.Resampling.LANCZOS)
        icon.paste(scaled_icon_char, ((icon_size - icw) // 2, (icon_size - ich) // 2), scaled_icon_char)
        icon.save(os.path.join(folder, 'ic_launcher.webp'), 'WEBP', quality=100)

        # 5. Round launcher icon
        mask = Image.new('L', (icon_size, icon_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, icon_size, icon_size), fill=255)
        round_icon = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))
        round_icon.paste(icon, (0, 0))
        round_icon.putalpha(mask)
        round_icon.save(os.path.join(folder, 'ic_launcher_round.webp'), 'WEBP', quality=100)

        print(f"Generated icons for {dens}")

if __name__ == '__main__':
    main()
