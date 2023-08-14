import tkinter as tk
from tkinter import ttk

# Create a Progress Bar that get deactivated and reactivated everytime we push the button download
# Définir la couleur de fond de la barre de progression
style = ttk.Style()
style.configure("Custom.TProgressbar", background="white")  

# Variables du téléchargement
total_downloads = 5
current_download = 0

# Fonction de simulation de téléchargement
def simulate_download():
    global current_download

    # Réinitialiser les variables du téléchargement
    current_download = 0

    start_button.configure(state="disabled")  # Désactiver le bouton de téléchargement
    progressbar.pack()
    percentage_label.pack()
    download_label.pack()

    def perform_download():
        global current_download

        current_download += 1
        download_label["text"] = f"Téléchargement {current_download}"
        progress = int((current_download / total_downloads) * 100)
        progressbar["value"] = progress
        percentage_label["text"] = f"{progress}%"
        root.update_idletasks()

        if current_download < total_downloads:
            root.after(1000, perform_download)
        else:
            progressbar.pack_forget()
            percentage_label.pack_forget()
            summary_label["text"] = "Téléchargement terminé !"
            summary_label.pack()

            # Supprimer le résumé après 2 secondes
            root.after(2000, lambda: summary_label.pack_forget())
            root.after(2000, lambda: download_label.pack_forget())

            start_button.configure(state="normal")  # Réactiver le bouton de téléchargement

    # Démarrer le téléchargement
    perform_download()

# Création de la fenêtre tkinter
root = tk.Tk()

# Création de la barre de progression
progressbar = ttk.Progressbar(root, mode="determinate", style="Custom.TProgressbar")

# Création du label pour afficher le pourcentage
percentage_label = tk.Label(root, text="0%")

# Création du label pour afficher les téléchargements
download_label = tk.Label(root, text="")

# Création du label pour afficher le résumé du téléchargement
summary_label = tk.Label(root, text="")

# Bouton pour déclencher le téléchargement
start_button = tk.Button(root, text="Démarrer le téléchargement", command=simulate_download)
start_button.pack()

# Lancement de la boucle principale de tkinter
root.mainloop()
