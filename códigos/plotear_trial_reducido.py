import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV reducido (editá esta línea con tu archivo)
csv_path = r"muestras\mayo\9\Trial_11_REDUCIDO.csv"

# Leer el CSV reducido
# Se asume que tiene columnas: 'tiempo', 'EMG 4', 'EMG 1', 'EMG 2', 'EMG 3'
df = pd.read_csv(csv_path)

# Crear figura y ejes\ nplt.figure(figsize=(10, 6))  # tamaño ajustable

# Plotear cada señal EMG vs tiempo
plt.plot(df['tiempo'], df['EMG 4'], label='EMG 4')
plt.plot(df['tiempo'], df['EMG 1'], label='EMG 1')
plt.plot(df['tiempo'], df['EMG 2'], label='EMG 2')
plt.plot(df['tiempo'], df['EMG 3'], label='EMG 3')

# Configuración del gráfico
plt.xlabel('Tiempo (s)')
plt.ylabel('EMG (mV)')
plt.title('Señales EMG vs Tiempo')
plt.legend()
plt.grid(True)

# Mostrar el plot
plt.tight_layout()
plt.show()