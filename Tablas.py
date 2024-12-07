import numpy as np
import pandas as pd

entradas = ["S1", "S2", "S3", "S4", "S5"]

# (32 combinaciones para 5 bits)
combinaciones = np.array(np.meshgrid([0, 1], [0, 1], [0, 1], [0, 1], [0, 1])).T.reshape(-1, 5)

# Crear DataFrame con las combinaciones
tabla_verdad = pd.DataFrame(combinaciones, columns=entradas)

def calcular_salidas(filas):
    S1, S2, S3, S4, S5 = filas
    # Reglas (puedes modificarlas según tu problema)
    if S1 == S2 == S3 == S4 == S5:  # Todos iguales
        return [1, 1, 1, 1]
    elif sum([S1, S2, S3, S4, S5]) == 3:  # 3 cerrados
        return [1, 0, 1, 0]
    elif sum([S1, S2, S3, S4, S5]) == 1:  # Solo 1 cerrado
        return [0, 1, 0, 0]
    elif sum([S1, S2, S3, S4, S5]) == 2:  # Solo 2 cerrados
        return [0, 0, 0, 0]
    else:
        return [0, 0, 0, 0]  # Por defecto, todas apagadas

tabla_verdad[["B1", "B2", "B3", "B4"]] = tabla_verdad.apply(calcular_salidas, axis=1, result_type="expand")

# archivo CSV
tabla_verdad.to_csv("tabla_verdad.csv", index=False)

# Mostrar la tabla
print(tabla_verdad)
