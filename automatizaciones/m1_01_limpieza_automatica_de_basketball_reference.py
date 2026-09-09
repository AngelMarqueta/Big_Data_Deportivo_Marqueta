"""Limpieza automática de Basketball Reference.

Lee un CSV, conserva los nulos como datos ausentes y normaliza nombre y posición sin depender de variables externas.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df['Player'] = df['Player'].astype('string').str.split('\\').str[0]
    df['Pos'] = df['Pos'].astype('string').str.split('-').str[0]
    return df
