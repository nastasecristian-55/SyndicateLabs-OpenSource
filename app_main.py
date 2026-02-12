import customtkinter as ctk
import webbrowser
import os
import chem_backend 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("SyndicateLabs v1.0 - Open Source Edition")
app.geometry("700x600")

molecule_library = {} 

def add_molecule():
    name = entry_name.get()
    smiles = entry_smiles.get()
    
    if not name or not smiles:
        log_to_console("Error: Name or SMILES missing.")
        return

    report, success = chem_backend.calculate_lipinski(name, smiles)
    
    if success:
        molecule_library[name] = smiles
        log_to_console(f"Analyzed & Added: {name}")
        text_results.insert("end", report)
        entry_name.delete(0, "end")
        entry_smiles.delete(0, "end")
    else:
        log_to_console(report)

def run_3d_viz():
    if not molecule_library:
        log_to_console("Library is empty! Add molecules first.")
        return
        
    log_to_console("Generating 3D Models... Please wait.")
    try:
        file_path = chem_backend.generate_3d_html(molecule_library)
        log_to_console(f"Success! Opening {file_path}...")
        
     
        webbrowser.open('file://' + os.path.realpath(file_path))
    except Exception as e:
        log_to_console(f"3D Error: {e}")

def log_to_console(message):
    lbl_status.configure(text=message)

lbl_title = ctk.CTkLabel(app, text="Lipinski & Pharmacophore Analyzer", font=("Roboto", 20, "bold"))
lbl_title.pack(pady=10)

frame_input = ctk.CTkFrame(app)
frame_input.pack(pady=10, padx=20, fill="x")

entry_name = ctk.CTkEntry(frame_input, placeholder_text="Molecule Name (e.g., Aspirin)", width=200)
entry_name.grid(row=0, column=0, padx=10, pady=10)

entry_smiles = ctk.CTkEntry(frame_input, placeholder_text="Paste SMILES String", width=400)
entry_smiles.grid(row=0, column=1, padx=10, pady=10)

btn_add = ctk.CTkButton(frame_input, text="Analyze & Add", command=add_molecule, fg_color="#D81B60", hover_color="#AD1457")
btn_add.grid(row=0, column=2, padx=10, pady=10)

text_results = ctk.CTkTextbox(app, width=650, height=300, font=("Consolas", 12))
text_results.pack(pady=10)
text_results.insert("0.0", "--- Results Log ---\n")

btn_viz = ctk.CTkButton(app, text="Generate 3D Pharmacophore View (Browser)", 
                        command=run_3d_viz, 
                        height=40, width=300, 
                        fg_color="#8E24AA",
                        hover_color="#6A1B9A")
btn_viz.pack(pady=10)

lbl_status = ctk.CTkLabel(app, text="Ready", text_color="gray")
lbl_status.pack(pady=5)
lbl_footer = ctk.CTkLabel(app, 
                          text="Created by Cristian Năstase © 2026 | Open Source v1.0", 
                          font=("Arial", 10), 
                          text_color="gray50")
lbl_footer.pack(side="bottom", pady=(0, 10))

app.mainloop()
