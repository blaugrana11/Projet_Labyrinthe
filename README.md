# Projet Labyrinthe
Projet labyrinthe Q2 Nabil et Mohamed (21168, 20130)

## Bibliothèque
Au cours de notre programmation, nous avons utilisé plusieurs bibliothèques, parmi lesquelles figurent la bibliothèque json de Python, qui offre des fonctionnalités pour coder et décoder des objets JSON. Elle est particulièrement pratique pour transférer et récupérer des données structurées. La bibliothèque socket de Python, de son côté, permet la communication en réseau entre ordinateurs. Elle fournit une interface pour établir des sockets, qui sont des points de connexion entre les programmes de différents ordinateurs. Les sockets peuvent être utilisés pour échanger des données entre ordinateurs, envoyer des messages à un serveur, etc. Enfin, la bibliothèque sys de Python propose des fonctions et des variables qui facilitent l'interaction avec le système d'exploitation. Elle permet notamment d'accéder à des informations système telles que les arguments de la ligne de commande. Nous l'utilisons aussi  pour envoyer le numéro de port sur le terminal lors du lancement de l'IA. Nous avons aussi eu besoin de la bibliothèque random car les différentes portes par lesquelles sont insérées les tuiles sont choisies aléatoirement.

## Stratégie
Notre stratégie consiste simplement à vérifier les passages accessibles et vérifier si la seconde tuile peut ou pas accueillir le pion en fonction de ses murs. Nous avons donc utilisé pour cela une boucle for ainsi que des if, elif, ... Et nous avons pris en compte les bordures du jeu afin que le pion ne se trouve pas sur une case qui n'existe pas. Tout cela étant dans une fonction, je n'ai plus qu'à l'appeler lorsque je reçois une requete "play".

