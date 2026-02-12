# 🧪 SyndicateLabs v1.0

**Lightweight Cheminformatics for the Modern Lab.** *Developed by Cristian Năstase*

---

## 🔬 What is it?
[cite_start]SyndicateLabs is a tool I built to bridge the gap between flat 2D chemical strings and 3D molecular reality. [cite: 27, 36, 138] [cite_start]It targets students and researchers who need a quick, no-fuss way to validate drug-likeness and visualize pharmacophores without opening heavy, expensive software. [cite: 26, 37, 144]

### Core Specs:
* [cite_start]**Lipinski & Veber Screening:** Fast calculation of MW, LogP, HBA, HBD, and TPSA. [cite: 39, 74, 75, 76, 77]
* [cite_start]**Interactive 3D:** Real-time generation of molecular conformers. [cite: 40, 92, 93, 94]
* [cite_start]**Smart Mapping:** Visual cues for Aromatic Rings (Blue), H-Donors (Magenta), and H-Acceptors (Cyan). [cite: 101, 102, 103]
* [cite_start]**Stability:** Custom RDKit embedding logic to prevent conformer crashes. [cite: 52]

---

## 📥 Getting Started

### 1. Standalone Apps (Easiest)
[cite_start]Grab the pre-built binaries from the **[Releases](../../releases)** tab. [cite: 43, 48]
* [cite_start]**Windows:** Unzip and run `SyndicateLabs.exe`. [cite: 44]
* [cite_start]**macOS:** Drag `SyndicateLabs.app` to your Applications folder. [cite: 49] (Right-click -> Open to bypass Gatekeeper)[cite_start]. [cite: 50, 51]

### 2. Developer Setup (Run from Source)
[cite_start]If you want to poke at the code, you'll need Python 3 and a few libraries. 

```bash
# Clone the repo
git clone [https://github.com/YOUR_USERNAME/SyndicateLabs.git](https://github.com/YOUR_USERNAME/SyndicateLabs.git)
cd SyndicateLabs

# Install the science
pip install -r requirements.txt

# Launch
python app_main.py
```
🛠 Tech Stack
GUI: CustomTkinter (Dark Mode by default) 

Brain: RDKit & Py3Dmol 

Environment: Developed on macOS for cross-platform utility. 

📄 License & Credits
License: MIT - Use it, fork it, learn from it. 

Context: Originally created as a final project for Didactica Domeniului at the University of Bucharest. 

Profesorul trăznit - over and out!
