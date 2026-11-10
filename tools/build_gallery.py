import base64
import os

with open(r'c:\Users\Naquib\Downloads\andee\images\mira_avatar_options_grid.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Mira Avatar Options</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f141c; color: #fff; padding: 24px; text-align: center; }}
  h1 {{ margin-bottom: 8px; color: #a78bfa; }}
  p {{ color: #94a1b2; font-size: 16px; margin-bottom: 20px; }}
  .grid-container {{ max-width: 960px; margin: 0 auto; box-shadow: 0 12px 40px rgba(0,0,0,0.6); border-radius: 16px; overflow: hidden; }}
  img {{ width: 100%; display: block; }}
  .options-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; max-width: 960px; margin: 24px auto; text-align: left; }}
  .card {{ background: #161b26; border: 1px solid #2e3440; border-radius: 12px; padding: 16px; }}
  .card h3 {{ margin: 0 0 8px 0; color: #38bdf8; }}
  .card p {{ font-size: 14px; margin: 0; color: #cbd5e1; line-height: 1.5; }}
</style>
</head>
<body>
  <h1>Mira Avatar Concepts (All 4 Options)</h1>
  <p>Compare all 4 designs below and choose which one you want as Mira's official avatar.</p>
  <div class="grid-container">
    <img src="data:image/jpeg;base64,{b64}" alt="Mira Avatar Comparison Grid" />
  </div>
  <div class="options-row">
    <div class="card">
      <h3>Option 1: Cosmic Violet</h3>
      <p>Indigo-violet sphere with glowing cyan ears and starry twilight anime eyes.</p>
    </div>
    <div class="card">
      <h3>Option 2: Pearl White</h3>
      <p>Minimalist glossy pearl white orb with pastel aurora rim glow and floating halo.</p>
    </div>
    <div class="card">
      <h3>Option 3: Golden Cyber</h3>
      <p>Dark titanium cybernetic orb with radiant amber-gold accents and digital emoji face.</p>
    </div>
    <div class="card">
      <h3>Option 4: Cozy Sprite</h3>
      <p>Pastel lavender-blue cloud fairy with starlight antenna and warm soft chibi look.</p>
    </div>
  </div>
</body>
</html>'''

with open(r'c:\Users\Naquib\Downloads\andee\images\mira_avatar_options.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(r'C:\Users\Naquib\.gemini\antigravity\brain\eaf39170-d147-4c3e-80c4-8839d0ddb824\mira_avatar_options.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML gallery created successfully')
