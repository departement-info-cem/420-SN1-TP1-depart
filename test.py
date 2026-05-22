

from racine import *
# A compléter par vous, changez, ajoutez des cas pour pouvoir tester souvent votre code.
# si un test du prof ne passe pas, tu peux le ramener ici pour expérimenter et déboguer.

racine_dicho(1, -5)

# un premier test la racine de 9 devrait être 3
resultat = racine_dicho(9)
print(resultat)
print(" réussite ? ", resultat == 3.0)

# un premier test la racine de 2 avec une seule décimale, devrait être 1.4
resultat = racine_dicho(2, -1)
print(resultat)
print(" réussite ? ", resultat == 1.4)
