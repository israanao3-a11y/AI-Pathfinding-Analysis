import time
import tracemalloc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import heapq
from math import pi

# Importation des fonctions de visualisation et des algorithmes
from visualization import (
    plot_radar_chart, plot_boxplots, 
    plot_pie_charts, plot_performance_comparison
)
from algorithms import bfs, dfs, a_star, gbfs
from config_maze import width, height, start, goal, maze

def run_experiments(algorithms, runs=100):
    """
    Exécute chaque algorithme 'runs' fois et stocke les résultats
    (temps, mémoire, longueur du chemin) dans un DataFrame pandas.
    """
    results = []
    for name, algo in algorithms.items():
        for _ in range(runs):
            path, metrics = algo(start, goal)
            results.append({
                'Algorithm': name,
                'Time': metrics['time'][-1],
                'Memory': metrics['memoire'][-1],
                'Path Length': len(path),
                'Step times': metrics['time'],
                'Step memory': metrics['memoire']
            })
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Configuration des algorithmes via des fonctions lambda
    # Cela permet d'uniformiser l'appel pour les algorithmes informés et non-informés
    heuristic = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    algorithms = {
        'BFS': lambda s, g: bfs(s, g, maze),
        'DFS': lambda s, g: dfs(s, g, maze),
        'A*': lambda s, g: a_star(s, g, maze, heuristic),
        'GBFS': lambda s, g: gbfs(s, g, maze, heuristic)
    }

    # Exécution des expériences
    df = run_experiments(algorithms)

    # Analyse statistique : calcul de la moyenne et de l'écart-type
    stats = df.groupby('Algorithm').agg({
        'Time': ['mean', 'std'],
        'Memory': ['mean', 'std'],
        'Path Length': ['mean', 'std']
    })
    print(stats)

    # Appel des fonctions de visualisation pour afficher les résultats
   
    plot_radar_chart(df)
    plot_boxplots(df)
    plot_pie_charts(stats)
    plot_performance_comparison(stats)