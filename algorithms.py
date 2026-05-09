import time
import tracemalloc # Pour mesurer la consommation de mémoire
from collections import deque
import heapq

# 1. Définition des mouvements (Haut, Bas, Gauche, Droite)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 2. Fonction pour trouver les voisins valides
def get_neighbors(node, maze):
    """
    Examine les cases adjacentes et retourne celles qui ne sont pas des murs.
    """
    y, x = node
    valides = []
    for dy, dx in directions:
        prochain = (y + dy, x + dx)
        # On vérifie si la case est dans le dictionnaire et si c'est un chemin (0)
        if prochain in maze and maze[prochain] == 0:
            valides.append(prochain)
    return valides

# 3. Estimation de la distance (Heuristique)
def heuristic(a, b):
    """
    Calcule la distance de Manhattan entre deux points.
    Indispensable pour A* et Greedy Best-First Search.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(depart, cible, labyrinthe, heuristique):
    """
    Implémentation de l'algorithme A* pour la recherche du chemin optimal.
    f(n) = g(n) + h(n)
    """
    # 1. Initialisation des outils de mesure de performance
    metriques = {'time': [], 'memoire': []}
    tracemalloc.start()
    temps_debut = time.time()
    
    # 2. Initialisation des structures de données
    # open_set : file de priorité (coût_total, noeud_actuel)
    open_set = []
    # On ajoute le point de départ avec son coût initial
    heapq.heappush(open_set, (0 + heuristique(depart, cible), depart))
    
    # came_from : dictionnaire pour reconstruire le chemin final
    provenance = {depart: None}
    
    # g_score : dictionnaire stockant le coût réel depuis le départ
    score_g = {depart: 0}
    
    # 3. Boucle principale de recherche
    while open_set:
        # Extraire le noeud ayant le plus petit f_score
        _, actuel = heapq.heappop(open_set)
        
        # Enregistrement des mesures de performance à chaque étape
        metriques['time'].append(time.time() - temps_debut)
        # On récupère la mémoire utilisée en Kiloctets (KB)
        metriques['memoire'].append(tracemalloc.get_traced_memory()[1] / 1024)
        
        # Si nous avons atteint la cible (l'objectif)
        if actuel == cible:
            break
            
        # Exploration des voisins du noeud actuel
        for voisin in get_neighbors(actuel, labyrinthe):
            # tentative_g : le coût pour atteindre ce voisin via le noeud actuel
            tentative_g = score_g[actuel] + 1
            
            # Si le chemin vers ce voisin est nouveau ou plus court que le précédent
            if voisin not in score_g or tentative_g < score_g[voisin]:
                provenance[voisin] = actuel
                score_g[voisin] = tentative_g
                
                # f(n) = g(n) + h(n)
                score_f = tentative_g + heuristique(voisin, cible)
                heapq.heappush(open_set, (score_f, voisin))
                
    tracemalloc.stop()
    
    # 4. Reconstruction du chemin final (du but vers le départ)
    chemin = []
    actuel_temp = cible
    while actuel_temp is not None:
        chemin.append(actuel_temp)
        actuel_temp = provenance.get(actuel_temp)
        
    # On inverse le chemin pour qu'il aille du départ vers la cible
    return chemin[::-1], metriques
def gbfs(depart, cible, labyrinthe, heuristique):
    """
    Implémentation de l'algorithme Greedy Best-First Search.
    Utilise uniquement l'heuristique h pour la priorité.
    """
    metriques = {'time': [], 'memoire': []}
    tracemalloc.start()
    temps_debut = time.time()

    # File de priorité avec (heuristique, noeud)
    open_set = []
    heapq.heappush(open_set, (heuristique(depart, cible), depart))
    provenance = {depart: None}

    while open_set:
        _, actuel = heapq.heappop(open_set)
        
        # Enregistrement des performances
        metriques['time'].append(time.time() - temps_debut)
        metriques['memoire'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if actuel == cible:
            break
        for voisin in get_neighbors(actuel, labyrinthe):
            if voisin not in provenance:
                provenance[voisin] = actuel
                priorite = heuristique(voisin, cible)
                heapq.heappush(open_set, (priorite, voisin))
    tracemalloc.stop()
    # Reconstruction du chemin
    chemin = []
    actuel_temp = cible
    while actuel_temp:
        chemin.append(actuel_temp)
        actuel_temp = provenance.get(actuel_temp)
    return chemin[::-1], metriques
def bfs(depart, cible, labyrinthe):
    """
    Implémentation de l'algorithme Breadth-First Search (BFS).
    Utilise une file (deque) pour une exploration niveau par niveau.
    """
    metriques = {'time': [], 'memoire': []}
    tracemalloc.start()
    temps_debut = time.time()

    file = deque([depart])
    provenance = {depart: None}

    while file:
        actuel = file.popleft()
        
        metriques['time'].append(time.time() - temps_debut)
        metriques['memoire'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if actuel == cible:
            break

        for voisin in get_neighbors(actuel, labyrinthe):
            if voisin not in provenance:
                provenance[voisin] = actuel
                file.append(voisin)

    tracemalloc.stop()
    chemin = []
    actuel_temp = cible
    while actuel_temp:
        chemin.append(actuel_temp)
        actuel_temp = provenance.get(actuel_temp)
    return chemin[::-1], metriques

def dfs(depart, cible, labyrinthe):
    """
    Implémentation de l'algorithme Depth-First Search (DFS).
    Utilise une pile (stack) pour explorer en profondeur.
    """
    metriques = {'time': [], 'memoire': []}
    tracemalloc.start()
    temps_debut = time.time()

    pile = [depart]
    provenance = {depart: None}

    while pile:
        actuel = pile.pop()
        
        metriques['time'].append(time.time() - temps_debut)
        metriques['memoire'].append(tracemalloc.get_traced_memory()[1] / 1024)

        if actuel == cible:
            break

        for voisin in get_neighbors(actuel, labyrinthe):
            if voisin not in provenance:
                provenance[voisin] = actuel
                pile.append(voisin)

    tracemalloc.stop()
    chemin = []
    actuel_temp = cible
    while actuel_temp:
        chemin.append(actuel_temp)
        actuel_temp = provenance.get(actuel_temp)
    return chemin[::-1], metriques
    