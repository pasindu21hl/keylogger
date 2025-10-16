# Keylogger Project

> **Warning — Educational Use Only:**
> This repository contains code that demonstrates techniques for capturing keystrokes, screenshots, and microphone audio. The version provided here is intended **strictly for education and research** on systems you own or where you have explicit written permission. Developing, distributing, or running functioning surveillance software on devices you do not own or do not have permission to test is unethical and may be illegal in your jurisdiction.

---

## Table of Contents
- [Overview](#overview)  
- [Safety & Legal Notice](#safety--legal-notice)  
- [Repository Contents](#repository-contents)  
- [Requirements](#requirements)  
- [Setup (local)](#setup-local)  
- [Configuration](#configuration)  
- [How to Run (Safe Mode)](#how-to-run-safe-mode)  
- [Testing & Sandboxing Recommendations](#testing--sandboxing-recommendations)  
- [.gitignore Suggestions](#gitignore-suggestions)  
- [Contributing](#contributing)  
- [License](#license)

---

## Overview
This project demonstrates structural and programming patterns used to collect keyboard events, screenshots, and audio recordings. The public repository contains a **GitHub-safe** variant that replaces active capture routines with mocks or clear warnings so that code can be studied without enabling real surveillance.

---

## Safety & Legal Notice
- **Do not** run the working keylogger on any machine you do not own or have explicit written consent to test.  
- Laws on computer monitoring vary; you are responsible for legal compliance.  
- GitHub and other platforms may remove or restrict content classified as malware. Use the safe/demo version for publishing.

---

## Repository Contents
- `keylogger_safe.py` — Demonstrative, non-operational version suitable for publishing.  
- `requirements.txt` — Packages used during development (for reference).  
- `.gitignore` — Recommended ignore patterns.  
- `README.md` — This file.  

> Note: Do **not** publish files that contain real credentials, functioning surveillance code, or personally identifiable data.

---

## Requirements
- Python 3.8+ recommended.  
- Development dependencies (only if you run full capture locally and responsibly):
```
pyscreenshot
pynput
sounddevice
Pillow
scipy
```
The safe/demo variant may not require all of the above.

---

## Setup (local)
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-directory>
```
2. Create and activate a virtual environment:
- Windows (PowerShell):
```powershell
C:/path/to/python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies (if needed):
```bash
pip install -r requirements.txt
```

---

## Configuration
**Never** hard-code credentials in the repository.

Example using environment variables (do not commit `.env`):
```
EMAIL_ADDRESS=you@example.com
EMAIL_PASSWORD=your_app_password_or_placeholder
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

Read values in Python:
```python
import os
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
```

---

## How to Run (Safe Mode)
The repository includes a safe/demo script that shows program flow without capturing real user data.

Run:
```bash
python keylogger_safe.py
```

Safe mode:
- Simulates key events and logs to console or a local file.
- Creates dummy or placeholder media files instead of real screenshots/audio.
- Prints (or simulates) email-sending behavior rather than performing network operations.

---

## Testing & Sandboxing Recommendations
- Use an isolated virtual machine (VirtualBox, VMware) or disposable test environment for any live tests.  
- Use snapshots to revert changes.  
- Mock or stub network calls (e.g., mock `smtplib.SMTP`) when testing.  
- Avoid using real credentials during tests; use placeholders or blocked network access.

---

## .gitignore Suggestions
Add the following to `.gitignore`:
```
# Sensitive files
.env
*.env
*.pem
*.key

# Generated media
*.wav
*.png
*.jpg

# Python artifacts
__pycache__/
*.pyc
.venv/
.venv/**

# IDE files
.vscode/
.idea/
```

---

## Contributing
- Contributions must maintain an educational, non-operational stance.  
- Open issues or PRs should clearly state purpose and include safety notes.  
- Do not submit working surveillance code intended for real-world usage without explicit safeguards and documented consent workflows.

---

## License
Choose a license appropriate for your goals (e.g., MIT for permissive open-source). Add a `LICENSE` file to the repository. If you want a specific license text inserted, specify which license and it will be provided.

---

If you want, I can now generate the `keylogger_safe.py`, `.gitignore`, and `requirements.txt` files so they are ready to commit alongside this `README.md`.

