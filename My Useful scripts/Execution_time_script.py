import time

# Enregistrer le temps de départ
start_time = time.time()

# Code à mesurer
for _ in range(10000000):
    pass

# Enregistrer le temps d'arrivée
end_time = time.time()

# Calculer le temps écoulé
elapsed_time = round(end_time,2) - round(start_time,2)
print("L'exécution du script a duré :", elapsed_time, "secondes")