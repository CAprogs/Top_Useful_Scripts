import tkinter as tk
import pandas as pd
import yaml

mangas_path = '/Users/charles-albert/Desktop/Manga Downloader/mangas.csv'
chapters_path = '/Users/charles-albert/Desktop/Manga Downloader/mangas_chapters.yml'
with open(chapters_path, 'r') as file:
        chapitres = yaml.safe_load(file)

def update_results(event):
    keyword = entry.get()
    cleaned_datas = datas['name'].fillna('')  # Remplacer les valeurs manquantes par une chaîne vide
    results = cleaned_datas[cleaned_datas.str.contains(keyword, case=False)]
    result_list = results.tolist()  # Convertir les résultats en liste
    result_box.delete(0, tk.END)  # Effacer le contenu précédent de la liste
    for result in result_list:
        result_box.insert(tk.END, result)  # Insérer chaque résultat dans la liste

def on_select(event):
    selected_indices = result_box.curselection()  # Récupérer les indices des éléments sélectionnés
    selected_items = [result_box.get(index) for index in selected_indices]  # Récupérer les éléments sélectionnés
    if not selected_items:
        print("liste vide")
    else:
        print(selected_items)
        manga_name = selected_items[0]
        try:
            update_chapters(manga_name)
        except:
            print("aucun manga sélectionné")

def update_chapters(manga_name):
    global chapitres
    if manga_name in chapitres:
        chapters = chapitres[manga_name]
        chapters_box.delete(0, tk.END)  # Effacer le contenu précédent de la liste déroulante
        for chapter in chapters:
            chapters_box.insert(tk.END, chapter)  # Insérer chaque chapitre dans la liste déroulante

def on_chapters_select(event):
    global selected_chapters
    selected_chapters = chapters_box.curselection()  # Récupérer les indices des chapitres sélectionnés
    selected_items = [chapters_box.get(index) for index in selected_chapters]  # Récupérer les chapitres sélectionnés
    print(selected_items)

# Créer une fenêtre Tkinter
window = tk.Tk()

# Créer une étiquette et une entrée pour la barre de recherche
label = tk.Label(window, text="Rechercher un manga :")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Créer une scrollbar pour la liste des résultats
result_scrollbar = tk.Scrollbar(window)
result_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Créer une liste pour afficher les résultats
result_box = tk.Listbox(window, selectmode=tk.SINGLE)
result_box.pack(side=tk.LEFT)
result_scrollbar.config(command=result_box.yview)
result_box.config(yscrollcommand=result_scrollbar.set, bd=0)

# Créer une scrollbar pour la liste des chapitres
chapters_scrollbar = tk.Scrollbar(window)
chapters_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Créer une liste déroulante pour afficher les chapitres
chapters_box = tk.Listbox(window, selectmode=tk.MULTIPLE)
chapters_box.pack(side=tk.RIGHT)
chapters_scrollbar.config(command=chapters_box.yview)
chapters_box.config(yscrollcommand=chapters_scrollbar.set,bd=0)

# Créer une variable pour stocker la sélection
selected_variable = tk.StringVar()
selected_label = tk.Label(window, textvariable=selected_variable)
selected_label.pack()

# Chargement des datas
datas = pd.read_csv(mangas_path)

# Associer l'événement '<KeyRelease>' à la fonction de mise à jour des résultats
entry.bind('<KeyRelease>', update_results)

# Associer l'événement '<ListboxSelect>' à la fonction de capture de la sélection
result_box.bind('<<ListboxSelect>>', on_select)

# Associer l'événement '<ListboxSelect>' à la fonction de capture de la sélection des chapitres
chapters_box.bind('<<ListboxSelect>>', on_chapters_select)

# Lancer la boucle principale Tkinter
window.mainloop()