import re
import os

def update_xml_strings(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        content = f.read()

    def repl(m):
        full = m.group(0)
        if 'codeflying' in full or 'trendshift' in full or 'http' in full:
            return full
        return full.replace('Mira', 'Mira')

    new_content = re.sub(r'<string\b[^>]*>.*?</string>', repl, content, flags=re.DOTALL)

    if 'ball_look_mira' not in new_content and 'ball_look_mira' in new_content:
        nl = '\r\n' if '\r\n' in new_content else '\n'
        new_content = new_content.replace(
            f'<string name="ball_look_mira">Mira</string>',
            f'<string name="ball_look_mira">Mira</string>{nl}    <string name="ball_look_mira">Mira</string>'
        )

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(new_content)
    print(f'Updated {path}')

def update_properties(path):
    with open(path, 'r', encoding='utf-8', newline='') as f:
        lines = f.readlines()

    nl = '\r\n' if lines and '\r\n' in lines[0] else '\n'
    new_lines = []
    has_mira_look = False
    for line in lines:
        if 'ball_look_mira=' in line:
            has_mira_look = True
        if not line.startswith('s_codeflying_url='):
            line = line.replace('Mira', 'Mira')
        new_lines.append(line)
        if line.startswith('ball_look_mira='):
            if not has_mira_look:
                new_lines.append(f'ball_look_mira=Mira{nl}')
                has_mira_look = True

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.writelines(new_lines)
    print(f'Updated {path}')

if __name__ == '__main__':
    update_xml_strings('app/src/main/res/values-en/strings.xml')
    update_xml_strings('app/src/main/res/values/strings.xml')
    update_properties('desktop/src/main/resources/strings_en.properties')
    update_properties('desktop/src/main/resources/strings_zh.properties')
