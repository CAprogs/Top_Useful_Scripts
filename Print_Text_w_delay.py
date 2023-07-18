import time

def print_slow(text, delay):
    for char in text:
        print(char, end='', flush=True)  # Imprime le caractère sans saut de ligne
        time.sleep(delay)  # Délai entre chaque caractère

# Exemple d'utilisation
text = "Le vent soufflait doucement à travers les arbres, faisant danser les feuilles colorées dans une valse hypnotique."
delay = 0.1  # Délai en secondes (0.1 seconde dans cet exemple)

print_slow(text, delay)