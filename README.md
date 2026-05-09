Analyse de Performance des Algorithmes de Pathfinding 🚀
Ce projet propose une étude comparative approfondie de plusieurs algorithmes de recherche de chemin (Pathfinding) implémentés en Python. L'objectif est d'évaluer leur efficacité relative en fonction du temps d'exécution, de la consommation de mémoire et de l'optimalité du chemin trouvé.

📊 Algorithmes Étudiés
Nous avons comparé quatre approches fondamentales de l'intelligence artificielle :

BFS (Breadth-First Search) : Recherche en largeur pour garantir le chemin le plus court.

DFS (Depth-First Search) : Recherche en profondeur.

A (A-Star)* : Algorithme heuristique performant pour l'optimisation.

GBFS (Greedy Best-First Search) : Recherche gloutonne basée sur l'heuristique.

📈 Visualisation des Résultats
Le projet génère automatiquement plusieurs graphiques pour interpréter les données collectées par Pandas :

1. Analyse Comparative Globale (Radar Chart)
Ce graphique permet de visualiser d'un seul coup d'œil les compromis (trade-offs) entre temps et mémoire pour chaque algorithme.

2. Répartition des Ressources (Pie Charts)
Ces diagrammes montrent la distribution proportionnelle du temps et de la mémoire consommée.

3. Comparaison Statistique (Bar & Box Plots)
Visualisation de la moyenne et de la variance des performances sur plusieurs tests.

🛠️ Technologies Utilisées
Python 3.x

Matplotlib & Seaborn : Pour la création de visualisations graphiques avancées.

Pandas : Pour la manipulation et l'analyse statistique des données.

Git/GitHub : Pour le versioning et le déploiement du projet.

📂 Structure du Projet
main.py : Point d'entrée pour lancer les expérimentations.
# Visualisation des Résultats

![Radar Chart](./radar_chart.png)
![Pie Charts](./pie_charts.png)
![Box Plots](./boxplots.png)
![Comparison](./performance_comparison.png)

algorithms.py : Implémentation des logiques de recherche.

visualization.py : Scripts de génération des graphiques.

config_maze.py : Configuration de l'environnement et du labyrinthe.
