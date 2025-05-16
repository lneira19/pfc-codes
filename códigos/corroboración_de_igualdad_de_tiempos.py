import pandas as pd

# Ruta al archivo CSV (valores separados por comas)
csv_path = r"muestras\mayo\9\Trial_12.csv"  # Usa una raw string para evitar errores de escape

# Número de líneas de encabezado a saltar (rows 1-7)
skip_header = 7

# Índices 0-based de las columnas de tiempo a comparar
time_cols = [0, 14, 28, 42]  # columnas 1, 15, 29, 43 en 1-based

# Nombre de columnas para reporte
time_names = ['tiempo 4', 'tiempo 1', 'tiempo 2', 'tiempo 3']


def read_csv_manual(path: str, skip_rows: int) -> list:
    """
    Lee un archivo de texto separado por comas,
    devolviendo una lista de filas (listas de floats),
    ignorando las primeras skip_rows líneas.
    Campos vacíos se interpretan como 0.0.
    """
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < skip_rows:
                continue
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(',')]
            nums = []
            for p in parts:
                nums.append(0.0 if p == '' else float(p))
            rows.append(nums)
    return rows


def report_diferentes(path: str):
    """
    Verifica desde la fila 8 si las columnas de tiempo son iguales.
    Imprime sólo las filas donde difieren.
    """
    rows = read_csv_manual(path, skip_header)
    for j, row in enumerate(rows):
        original_fila = skip_header + j + 1
        values = [row[idx] if idx < len(row) else None for idx in time_cols]
        # Todas deben existir y ser iguales
        if None in values or len(set(values)) != 1:
            # Reporte de discrepancia
            detalles = {name: (values[i] if i < len(values) else None) 
                        for i, name in enumerate(time_names)}
            print(f"Fila {original_fila} DIFERENTES: {detalles}")

if __name__ == '__main__':
    report_diferentes(csv_path)
