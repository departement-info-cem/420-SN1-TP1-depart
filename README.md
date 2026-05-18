# 420-SN1-TP1-depart
Dépôt de départ pour le TP1.

## Pointage

1 point : documentation de ton code : commits et docstring. 

3 points : dichotomie avec arrondi
- vous avez implanté le calcul de la racine carrée
- vous avez validé sur des valeurs comme 0, 1, 0.000001, 9, 0.9999999, un grand nombre etc.
  - par exemple la racine de 2 vaut .....
- vous avec validé avec différent degré de précision
  - par exemple la racine de 2 avec une précision de 1 vaut 1.4 
- les profs fournissent

3 points : chiffre par chiffre
- vous avez implanté le calcul
- vous avez validé avec le

1 point : comparez les performances:
- on souhaite comparer les performances de tes 2 solutions avec la fonction python fournie (math.sqrt)
- on veut que tu définisses une fonction **perf** qui prend 2 paramètres tous les deux optionnels:
  - borneMax avec une valeur par défaut qui soit le plus grand nombre float possible en Python (petite recherche Google ici)
  - nombreAppels avec une valeur par défaut de 10000
- la fonction doit pour chaque fonction mesurer le temps nécessaire pour calculer les racines carrées de nombreAppels nombres, tous tirés entre 1 et borneMax. Pour chaque fonction on veut le temps total pour tous les appels, le temps moyen par appel.
- exemple d'affichage pour un appel de perf avec borneMax 1.0, nombreAppels de 1000 (valeurs aberrantes)
```
Performance des trois méthodes pour 1000 nombres entre 0.0 et 1.0
math.sqrt           total : 1001ms          moyen: 1.001ms
dichotomie          total : 1001ms          moyen: 1.001ms
chiffres            total : 1001ms          moyen: 1.001ms
```


1 point : vous devez choisir une de vos 2 méthodes et l'adapter au calcul de la racine nième

1 point : racine précise
- dans tes solutions précédentes, tu as fixé une précision pour faciliter la solution
- mais dans les faits, on veut avoir la meilleure racine carrée possible
- produis une racine carrée la plus précise possible en réflechissant à quand et comment ta solution doit s'arrêter
- tu peux partir de l'algorithme de ton choix.

