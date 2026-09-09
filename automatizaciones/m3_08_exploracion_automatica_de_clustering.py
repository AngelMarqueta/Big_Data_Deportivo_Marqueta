"""Exploración automática de clustering.

Prueba varios valores de k y devuelve inercia y silhouette para apoyar, no sustituir, la decisión analítica.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def explore_cluster(X, valores_k=range(2, 9), random_state=42):
    resultados = []
    for k in valores_k:
        modelo = KMeans(n_clusters=k, n_init=20, random_state=random_state)
        etiquetas = modelo.fit_predict(X)
        resultados.append({'k': k, 'inercia': modelo.inertia_,
                           'silhouette': silhouette_score(X, etiquetas)})
    return pd.DataFrame(resultados)
