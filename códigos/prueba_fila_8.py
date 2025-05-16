import pandas as pd
import os

# Ruta al archivo CSV (sin encabezados)
csv_path = r"muestras\mayo\9\Trial_11.csv"  # Usa una raw string para evitar errores de escape

def extract_emg_tempos(csv_path: str) -> dict:
    """
    Lee un archivo de valores separados por comas (CSV) sin encabezados, toma la fila 8 (1-based)
    y extrae valores de columnas específicas.

    Columnas (1-based) y nombres:
      1  -> 'tiempo 4'
      2  -> 'EMG 4 (mv)'
      15 -> 'tiempo 1'
      16 -> 'EMG 1 (mv)'
      29 -> 'tiempo 2'
      30 -> 'EMG 2 (mv)'
      43 -> 'tiempo 3'
      44 -> 'EMG 3 (mv)'

    Devuelve un diccionario {nombre: valor}.
    """
    try:
        with open(csv_path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        raise RuntimeError(f"No se pudo abrir el archivo: {e}")

    if len(lines) < 8:
        raise ValueError("El archivo no tiene al menos 8 filas.")

    # Fila 8 (1-based), corresponde a índice 7
    fila_8 = lines[7].strip()
    valores = [v.strip() for v in fila_8.split(',')]

    # Mapeo de columna (1-based) a nombre de variable
    mapping = {
        1: 'tiempo 4',
        2: 'EMG 4 (mv)',
        15: 'tiempo 1',
        16: 'EMG 1 (mv)',
        29: 'tiempo 2',
        30: 'EMG 2 (mv)',
        43: 'tiempo 3',
        44: 'EMG 3 (mv)'
    }

    resultados = {}
    for col_1based, nombre in mapping.items():
        idx0 = col_1based - 1
        if 0 <= idx0 < len(valores):
            try:
                resultados[nombre] = float(valores[idx0])
            except ValueError:
                resultados[nombre] = valores[idx0]  # si no se puede convertir, lo dejamos como string
        else:
            resultados[nombre] = None  # Columna fuera de rango

    return resultados

if __name__ == '__main__':
    datos = extract_emg_tempos(csv_path)
    print("Valores extraídos de la fila 8:")
    for nombre, valor in datos.items():
        print(f"- {nombre}: {valor}")