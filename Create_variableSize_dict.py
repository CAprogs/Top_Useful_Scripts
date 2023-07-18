# Sauvegarder des dictionnaires avec des clés de différentes tailles
# =========================
# Methode 1 : Fichier yml
# =========================
import yaml

manga_chapters_dict = {'Naruto':[]} # le dictionnaire pouvait aussi etre vide dans ce cas utiliser #@
#@ manga_chapters_dict['Naruto']=[] 
manga_chapters_dict['Sasuke']=[]
manga_chapters_dict['Jujutsu']=[]
manga_chapters_dict['Naruto'].append('chapitre 1')
manga_chapters_dict['Naruto'].append('volume 3')
manga_chapters_dict['Sasuke'].append('volume 1')
manga_chapters_dict['Sasuke'].append('chapitre 6')
manga_chapters_dict['Jujutsu'].append('chapitre 3')
manga_chapters_dict['Jujutsu'].append('chapitre 1')

# Convertir le dictionnaire en document YAML
yml_data = yaml.dump(manga_chapters_dict)

# Écrire le document YAML dans un fichier
with open('/Users/charles-albert/Desktop/Manga Downloader/mangas_chapters.yml', 'w') as file:
    file.write(yml_data)

# =========================
# Methode 2 : Fichier csv
# =========================

import pandas as pd

manga_chapters_dict = {'Naruto':[]} # le dictionnaire pouvait aussi etre vide dans ce cas utiliser #@
#@ manga_chapters_dict['Naruto']=[] 
manga_chapters_dict['Sasuke']=[]
manga_chapters_dict['Jujutsu']=[]
manga_chapters_dict['Naruto'].append('chapitre 1')
manga_chapters_dict['Naruto'].append('volume 3')
manga_chapters_dict['Sasuke'].append('volume 1')
manga_chapters_dict['Sasuke'].append('chapitre 6')
manga_chapters_dict['Jujutsu'].append('chapitre 3')
manga_chapters_dict['Jujutsu'].append('chapitre 1')

# Convertir le dictionnaire en dataframe Pandas
datas = pd.DataFrame(manga_chapters_dict,dtype=str)

# Convertir le dataframe en fichier csv et le sauvegarder
datas.to_csv('/Users/charles-albert/Desktop/Manga Downloader/mangas_chapters.csv', index=False)
