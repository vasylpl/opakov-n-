import random
import time

def generuj_seznam(delka):
    return [random.randint(1, 100) for _ in range(delka)]

def vypis_seznam(seznam):
    print("Seznam:", seznam)

seznam = generuj_seznam(8)
vypis_seznam(seznam)

while True:
    time.sleep(5)  # Počkej 5 sekund
    seznam = generuj_seznam(8)
    vypis_seznam(seznam)