

from racine import *
# A compléter par vous, changez, ajoutez des cas pour pouvoir tester souvent votre code.


# un premier test la racine de 9 devrait être 3
resultat = racine_arrondi_dicho(9)
print(resultat)
print(" réussite ? ", resultat == 3.0)

# un premier test la racine de 2 avec une seule décimale, devrait être 1.4
resultat = racine_arrondi_dicho(2, 1)
print(resultat)
print(" réussite ? ", resultat == 1.4)
