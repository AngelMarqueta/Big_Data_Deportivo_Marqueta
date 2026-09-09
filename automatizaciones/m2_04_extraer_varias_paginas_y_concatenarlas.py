"""Extraer varias páginas y concatenarlas.

Recorre URLs de equipos o temporadas, añade trazabilidad y concatena solo resultados compatibles.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def extraer_temporadas(urls_por_temporada):
    partes = []
    for temporada, url in urls_por_temporada.items():
        tabla = extraer_tabla_fbref(url)
        tabla['temporada'] = temporada
        partes.append(tabla)
    if not partes:
        return pd.DataFrame()
    return pd.concat(partes, ignore_index=True, sort=False)
