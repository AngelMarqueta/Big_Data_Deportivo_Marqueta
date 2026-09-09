"""Descarga automática de eventos.

Obtiene los eventos de un partido mediante su match_id y conserva el identificador en la salida.

Este archivo es un patrón educativo: adapta nombres de columnas y valida una
muestra antes de usarlo en producción.
"""

def event_data(match_id):
    eventos = sb.events(match_id=match_id)
    if eventos.empty:
        raise ValueError(f'El partido {match_id} no contiene eventos')
    eventos['match_id'] = match_id
    return eventos
