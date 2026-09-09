"""Limpieza completa de datos InStat.

Automatiza sustitución de guiones, porcentajes y columnas numéricas. Corrige el original: se itera sobre df.columns, no sobre la variable global jug_2b.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def clean_data_instat(df, columnas_categoricas=None):
    df = df.copy().replace('-', pd.NA)
    columnas_categoricas = columnas_categoricas or [
        'Nombre', 'Posición', 'Equipo', 'Pierna',
        'Nacionalidad', 'Selección nacional'
    ]
    cols_pct = [col for col in df.columns if '%' in col]
    for col in cols_pct:
        df[col] = (pd.to_numeric(
            df[col].astype('string').str.replace('%', '', regex=False),
            errors='coerce') / 100)
    cols_num = [col for col in df.columns if col not in columnas_categoricas]
    for col in cols_num:
        if col not in cols_pct:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
