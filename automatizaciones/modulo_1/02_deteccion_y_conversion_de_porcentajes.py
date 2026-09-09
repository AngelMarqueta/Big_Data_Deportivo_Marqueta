"""Detección y conversión de porcentajes.

Localiza por nombre las columnas porcentuales y admite valores con %, guiones y nulos.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def convertir_porcentajes(df):
    df = df.copy()
    cols_pct = [col for col in df.columns if '%' in col]
    for col in cols_pct:
        texto = df[col].astype('string').str.replace('%', '', regex=False)
        df[col] = pd.to_numeric(texto.replace('-', pd.NA), errors='coerce') / 100
    return df
