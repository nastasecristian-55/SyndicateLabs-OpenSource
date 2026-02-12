# SyndicateLabs (Open Source Edition)

**A cross-platform computational chemistry tool for education and drug design.**
*Created by Cristian Năstase*

## Overview
SyndicateLabs is a desktop application designed to bridge the gap between 2D chemical structures and 3D molecular interactions. It helps students and researchers perform real-time **Lipinski Rule of 5** analysis and generate interactive **3D Pharmacophore models**.

## Key Features
* **Drug-Likeness Analysis:** Instant calculation of MW, LogP, HBA, HBD, and TPSA (Veber's Rules).
* **3D Visualization:** Generates interactive 3D models showing pharmacophores (Aromatic rings, H-Donors/Acceptors).
* **Robust Conformer Generation:** Uses advanced RDKit algorithms to handle complex molecules (e.g., Olanzapine) without crashing.
* **Cross-Platform:** Runs on macOS and Windows.

## Installation

### Option 1: Download the App (Recommended for Users)
You do not need to install Python to use this tool.
1. Go to the **[Releases](../../releases)** page of this repository.
2. Download the version for your OS:
   * **Windows:** Download `SyndicateLabs_Win.zip`, extract, and run `SyndicateLabs.exe`.
   * **Mac:** Download `SyndicateLabs_Mac.zip`, extract, move to Applications, and run `SyndicateLabs.app`.

### Option 2: Run from Source (Recommended for Developers)
If you want to modify the code or see how it works:
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SyndicateLabs.git](https://github.com/YOUR_USERNAME/SyndicateLabs.git)
   cd SyndicateLabs
   ```
2. **Install dependencies:**
  ```bash
    pip install -r requirements.txt
```
3. **Run the application:**
  ```bash
python app_main.py
```

Built With
Python 3 - Core Logic
CustomTkinter - Modern UI Framework
RDKit - Cheminformatics & Molecular Analysis
Py3Dmol - 3D Visualization

License
This project is open-source and available under the MIT License. You are free to use, modify, and distribute this software for educational and research purposes.

© 2026 Cristian Năstase. Developed for Didactica Domeniului.
