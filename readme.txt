Question 6 ] 

Tout d'abord on doit taper dans la ligne de commande : pip install pyproject.toml
Pour formater les codes en .py pour qu’il soit plus lisible avec black, la commande suivante est utilisée (pour tous les fichiers .py) : 
black --config= pyproject.toml src/fichier.py

Les imports sont organisés de la meilleure façon avec isort. Il y a le fichier test_sort.py (présent dans : src/test_sort.py) qui permet de trier es packages dans l'ordre.




