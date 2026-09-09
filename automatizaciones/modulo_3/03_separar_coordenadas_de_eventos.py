"""Separar coordenadas de eventos.

Extrae x e y con seguridad cuando location está ausente o incompleto.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def coordinates(df, columna='location'):
    df = df.copy()
    coords = df[columna].apply(
        lambda p: p if isinstance(p, (list, tuple)) and len(p) >= 2 else [pd.NA, pd.NA]
    )
    df[['x', 'y']] = pd.DataFrame(coords.tolist(), index=df.index)
    return df
