import subprocess

issues = [
    {
        "title": "[Feature]: Multi-language Voice Wake Word & Phoneme Templates",
        "labels": "enhancement,help wanted",
        "body": """### Summary
Mira features an entirely on-device offline wake word engine based on MFCC + Dynamic Time Warping (DTW) in `net.synxneuos.mira.wake.WakeWord`. 

### Objective
Enhance wake word enrollment to provide language-specific tuning and phonetic guidance for global languages:
- Hindi (e.g. 'नमस्ते मीरा' / 'सुनो मीरा')
- Spanish (e.g. 'Hola Mira')
- Japanese (e.g. 'ミラちゃん')
- French / German / Mandarin

### Details
- Optimize DTW thresholding for varied accents.
- Add multilingual enrollment guidance strings in `WakeEnrollUi.kt`.

Contributions from multilingual developers are warmly welcome!"""
    },
    {
        "title": "[Platform]: Native Windows Desktop Body support using Compose Desktop & UI Automation",
        "labels": "enhancement,help wanted",
        "body": """### Summary
Currently, `desktop/` targets macOS via a Swift native bridge (`desktop/native/MiraMac.swift`).
We want to bring native Windows PC support to Mira so she can run as an interactive companion on Windows 11/10 desktops!

### Proposed Architecture
1. Implement Windows Accessibility & UI tree reading via Windows UI Automation API (using JNA or C++ DLL).
2. Wire up screen tap/click, keystroke injection, and screen capture.
3. Hook into `desktop/src/main/kotlin/net/synxneuos/mira/desktop/` to run seamlessly on Windows.

If you have experience with Windows UI Automation / Win32 / Compose Desktop, we would love to collaborate!"""
    }
]

for iss in issues:
    cmd = [
        "gh", "issue", "create",
        "--repo", "Synxneuos/mira",
        "--title", iss["title"],
        "--label", iss["labels"],
        "--body", iss["body"]
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Created:", res.stdout.strip() if res.returncode == 0 else f"Err: {res.stderr}")
