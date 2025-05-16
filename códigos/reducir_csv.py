import pandas as pd
from pathlib import Path

# Ruta al archivo CSV (editá esta línea con tu archivo)
csv_path = r"muestras\mayo\9\Trial_11.csv"

# Número de líneas de encabezado a saltar
skip_header = 7

# Índices de las columnas a extraer (0-based)
cols = {
    'tiempo': 0,      # tiempo (todas las columnas iguales)
    'EMG 4': 1,
    'EMG 1': 15,
    'EMG 2': 29,
    'EMG 3': 43,
}

def reduce_csv(path: str, skip_header: int = 7) -> Path:
    """
    Lee un CSV, salta las primeras `skip_header` filas y extrae:
      - tiempo
      - EMG 4, 1, 2, 3
    Guarda un nuevo CSV con sufijo '_REDUCIDO'.
    """
    df = pd.read_csv(
        path,
        skiprows=skip_header,
        header=None,
        sep=',',
        skipinitialspace=True
    )

    reduced = pd.DataFrame()
    for name, idx in cols.items():
        if idx < df.shape[1]:
            reduced[name] = df.iloc[:, idx]
        else:
            reduced[name] = pd.Series(dtype=float)

    reduced = reduced.fillna(0.0)

    input_path = Path(path)
    output_path = input_path.with_name(f"{input_path.stem}_REDUCIDO.csv")
    reduced.to_csv(output_path, index=False)
    return output_path

if __name__ == '__main__':
    try:
        out = reduce_csv(csv_path, skip_header)
        print(f"Archivo reducido guardado en: {out}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
