import tkinter as tk
from tkinter import ttk

def on_selection(event):
    selected_item = combo_var.get()
    print("Élément sélectionné :", selected_item)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Liste déroulante")

# Créer une variable pour stocker la sélection
combo_var = tk.StringVar()

# Créer la liste déroulante (combobox)
combo_box = ttk.Combobox(root, textvariable=combo_var, state="readonly", height= 10,width= 10)
combo_box['values'] = ["Élément 1", "Élément 2", "Élément 3", "Élément 4"]
combo_box.bind("<<ComboboxSelected>>", on_selection)
combo_box.pack(padx=10, pady=10)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
