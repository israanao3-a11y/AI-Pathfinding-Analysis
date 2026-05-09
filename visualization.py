import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from math import pi

# 1. Graphique Radar (Radar Chart) pour une comparaison multidimensionnelle
def plot_radar_chart(df):
    """
    Crée un graphique en radar comparant les performances globales des algorithmes.
    """
    categories = ['Time', 'Memory', 'Path Length']
    num_vars = len(categories)

    # Normalisation des données entre 0 et 1 pour une comparaison équitable
    df_norm = df.groupby('Algorithm')[categories].mean()
    df_norm = df_norm / df_norm.max()

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1] # Fermer le cercle

    for algo in df['Algorithm'].unique():
        values = df_norm.loc[algo].tolist()
        values += values[:1]
        ax.plot(angles, values, marker='o', label=algo)
        ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title('Comparaison des Performances (Normalisée)')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.show()

# 2. Comparaison des moyennes par Bar Charts
def plot_performance_comparison(stats):
    """
    Crée des diagrammes à barres pour comparer le Temps, la Mémoire et la Longueur.
    """
    metrics = ['Time', 'Memory', 'Path Length']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, metric in enumerate(metrics):
        means = stats[(metric, 'mean')]
        stds = stats[(metric, 'std')]
        
        axes[i].bar(means.index, means, yerr=stds, capsize=5, color=sns.color_palette('Set2'))
        axes[i].set_title(f'Comparaison : {metric}')
        axes[i].set_ylabel(metric)
        axes[i].grid(True, axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# 3. Diagrammes en boîtes (Boxplots) pour la distribution
def plot_boxplots(df):
    """
    Visualise la distribution et la stabilité des résultats.
    """
    metrics = ['Time', 'Memory', 'Path Length']
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    for i, metric in enumerate(metrics):
        sns.boxplot(x='Algorithm', y=metric, data=df, ax=axes[i], palette='Set3')
        axes[i].set_title(f'Distribution de : {metric}')
        axes[i].grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

# 4. Diagrammes circulaires (Pie Charts)
def plot_pie_charts(stats):
    """
    Montre la proportion de chaque métrique consommée par chaque algorithme.
    """
    metrics = ['Time', 'Memory', 'Path Length']
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, metric in enumerate(metrics):
        means = stats[(metric, 'mean')]
        axes[i].pie(means, labels=means.index, autopct='%1.1f%%', startangle=140)
        axes[i].set_title(f'Répartition de : {metric}')

    
    plt.savefig('radar_chart.png')
    plt.show()
    plt.savefig('pie_charts.png')
    plt.show()
    plt.savefig('performance_comparison.png')
    plt.show()
    plt.savefig('boxplots.png')
    plt.show()