# 420-SN1-TP1-depart
Dépôt de départ pour le TP1.

## Structure

Vous trouverez 3 fichiers :
- racine.py contient le module de calcul de la racine (carrée, n-ième...)
  - ne contient que les fonctions du module
  - ne pas changer les noms des fonctions présentes
  - vous pouvez y créer des fonctions pour un sous-problème
- test.py contient les tests que vous mettrez en place pour tester, déboguer et valider votre code (on veut les exécuter souvent quand on code)
- testsProf.py contient certains appels au module racine que le prof va utiliser pour valider si votre code remplit les consignes
  - vous pouvez l'exécuter pour avoir un aperçu de votre progression
  - ATTENTION, il est difficile de déboguer ici car il y a beaucoup d'appels


## Pointage

1 point : documentation de votre code : commits et docstring.
- vous devez respecter le format de commit demandé; le titre et la description correspondent au travail effectué
- le docstring doit indiquer le calcul effectué, le type de retour, les paramètres, leurs rôles et leurs types
  - un exemple valide est fourni sur une fonction 
- le français est correct sur les docstring (orthographe et grammaire)

3 points : dichotomie avec arrondi
- vous avez implanté le calcul de la racine carrée
- vous avez validé sur des valeurs comme 0, 1, 0.000001, 9, 0.9999999, un grand nombre etc.
  - par exemple la racine de 2 vaut .....
- vous avez validé avec différents degrés de précision
  - par exemple la racine de 2 avec une précision de 1 vaut 1.4 
- les profs fournissent

3 points : chiffre par chiffre
- vous avez implanté le calcul
- vous avez validé avec les valeurs et précisions
- ATTENTION, pour avoir n chiffres, il se peut que vous en ayez besoin de n+1

1 point : comparez les performances :
- on souhaite comparer les performances de vos 2 solutions avec la fonction Python fournie (`math.sqrt`)
- on veut que vous définissiez une fonction **perf** qui prend 2 paramètres, tous les deux optionnels :
  - borneMax avec une valeur par défaut qui soit le plus grand nombre float possible en Python (petite recherche Google ici)
  - nombreAppels avec une valeur par défaut de 10000
- la fonction doit, pour chaque méthode, mesurer le temps nécessaire pour calculer les racines carrées de `nombreAppels` nombres, tous tirés entre 1 et `borneMax`. Pour chaque méthode, on veut le temps total pour tous les appels et le temps moyen par appel.
- exemple d'affichage pour un appel de perf avec borneMax 1.0, nombreAppels de 1000 (valeurs aberrantes)
```
Performance des trois méthodes pour 1000 nombres entre 0.0 et 1.0
math.sqrt           total : 1001ms          moyen: 1.001ms
dichotomie          total : 1001ms          moyen: 1.001ms
chiffres            total : 1001ms          moyen: 1.001ms
```


1 point : vous devez choisir une de vos 2 méthodes et l'adapter au calcul de la racine n-ième
- voir description

1 point : racine précise
- dans vos solutions précédentes, vous avez fixé une précision pour faciliter la solution
- mais dans les faits, on veut avoir la meilleure racine carrée possible
- produisez une racine carrée la plus précise possible en réfléchissant à quand et comment votre solution doit s'arrêter
- vous pouvez partir de l'algorithme de votre choix.

