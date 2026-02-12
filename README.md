# SyndicateLabs v1.0

**Lightweight Cheminformatics for the Modern Lab.** *Developed by Cristian Năstase*


**I. What is it**

SyndicateLabs is a tool I built to bridge the gap between flat 2D chemical strings and 3D molecular reality. 
It targets students and researchers who need a quick, no-fuss way to validate drug-likeness and visualize pharmacophores without opening heavy, expensive software.


**II. Core Specs:**
* **Lipinski & Veber Screening:** Fast calculation of MW, LogP, HBA, HBD, and TPSA;
* **Interactive 3D:** Real-time generation of molecular conformers;
* **Smart Mapping:** Visual cues for Aromatic Rings (Blue), H-Donors (Magenta), and H-Acceptors (Cyan);
* **Stability:** Custom RDKit embedding logic to prevent conformer crashes.


**III. Getting Started**

**1. Standalone Apps (Easiest)**
Grab the pre-built binaries from the **[Releases](../../releases)** tab. 
* **Windows:** Unzip and run `SyndicateLabs.exe`.
* **macOS:** Drag `SyndicateLabs.app` to your Applications folder. (Right-click -> Open to bypass Gatekeeper)

**2. Developer Setup (Run from Source)**
If you want to poke at the code, you'll need Python 3 and a few libraries. 

```bash
# Clone the repo
git clone [https://github.com/YOUR_USERNAME/SyndicateLabs.git](https://github.com/YOUR_USERNAME/SyndicateLabs.git)
cd SyndicateLabs

# Install the science
pip install -r requirements.txt

# Launch
python app_main.py
```

### Tech Stack

* **GUI:** CustomTkinter (Dark Mode by default); 
* **Brain:** RDKit & Py3Dmol; 
* **Environment:** Developed on macOS for cross-platform utility. 

### License & Credits

* **License:** MIT - Use it, fork it, learn from it; 
* **Context:** Originally created as a final project for Didactica Domeniului at the University of Bucharest.

  

***Profesorul trăznit - over and out!***
