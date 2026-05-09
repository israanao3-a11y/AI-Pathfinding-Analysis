# ==========================================================
# Configuration du labyrinthe
# ==========================================================
# Définir le labyrinthe aléatoirement :
import random
def generate_maze(width, height, path, start, goal):
    """
    Génère un labyrinthe aléatoire avec un chemin prédéfini, un point de départ et une arrivée.
    
    Parameters:
        width (int): La largeur du labyrinthe.
        height (int): La hauteur du labyrinthe.
        path (list of tuples): Un chemin prédéfini sous forme de liste de coordonnées (y, x).
        start (tuple): Le point de départ (y, x) du labyrinthe.
        goal (tuple): Le point d'arrivée (y, x) du labyrinthe.
        
    Returns:
        dict: Un dictionnaire représentant le labyrinthe.
    """
    
    maze = {}
    
    # Initialiser le labyrinthe avec des murs aléatoires (1) et des espaces ouverts (0)
    for y in range(height):
        for x in range(width):
            # Ici, on remplit tout de murs par défaut (1)
            maze[(y, x)] = 1 
            
    # S'assurer que le chemin prédéfini est ouvert (0)
    for coord in path:
        maze[coord] = 0
        
    # S'assurer que le point de départ et d'arrivée sont ouverts (0)
    maze[start] = 0
    maze[goal] = 0
    return maze
# Configuration de la grille (Dimensions)
width = 100   # Largeur de la grille
height = 10   # Hauteur de la grille

# Points de départ et d'arrivée (Coordonnées)
start = (0, 0)      # Point de départ
goal = (99, 9)      # Point d'arrivée (Cible)

# Construction du labyrinthe (Maze)
# 0 représente un chemin libre, 1 représente un mur (obstacle)
# Création d'une grille vide initialement
maze = [[0 for x in range(width)] for y in range(height)]

# Exemple pour ajouter des murs manuellement (Optionnel)
# maze[5][10] = 1
# maze[5][11] = 1
def initialize_path(path, width, height):
    """
    Initialise un chemin prédéfini pour garantir une solution dans le labyrinthe.
    """
    i, j = 0, 0
    
    # Premier segment vertical
    for i in range(0, height // 2):
        path.append((i, j))
    
    # Premier segment horizontal
    for j in range(0, int(width / 2)):
        path.append((i, j))
        
    # Deuxième segment vertical
    for i in range(0, height // 2):
        path.append((i, j))
        
    # Deuxième segment horizontal (vers la fin)
    for j in range(width // 2, width - 1):
        path.append((0, j))
        
    # Segment vertical final sur la dernière colonne
    for i in range(0, height):
        path.append((i, width - 1)) 
        
    return path
