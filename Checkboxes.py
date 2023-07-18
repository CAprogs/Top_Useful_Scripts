import tkinter as tk
# How to display some checkboxes in a TK window
def show_selected():
    selection = ""
    if var1.get():
        selection += "Option 1 "
    if var2.get():
        selection += "Option 2 "
    if var3.get():
        selection += "Option 3 "
    if var4.get():
        selection += "Option 4 "
    if selection == "":
        selection = "Aucune option sélectionnée"
    print(selection)

# Création de la fenêtre tkinter
root = tk.Tk()

# Création des variables pour le suivi des cases à cocher
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

# Création des cases à cocher
checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=var1)
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=var2)
checkbutton2.pack()

checkbutton3 = tk.Checkbutton(root, text="Option 3", variable=var3)
checkbutton3.pack()

checkbutton4 = tk.Checkbutton(root, text="Option 4", variable=var4)
checkbutton4.pack()

# Bouton pour afficher les options sélectionnées
button = tk.Button(root, text="Afficher la sélection", command=show_selected)
button.pack()

# Lancement de la boucle principale de tkinter
root.mainloop()
