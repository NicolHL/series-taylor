import math

def taylor_series_exp(x, n):
    """
    Calcula la aproximación de e^x usando la serie de Taylor hasta el término n-ésimo.
    
    Parámetros:
    x (float): El valor en el que se evalúa la función.
    n (int): El número de términos en la serie de Taylor.
    
    Retorna:
    float: La aproximación de e^x.
    """
    approximation = 0
    for i in range(n):
        approximation += x**i / math.factorial(i)
    return approximation

# Valores de x para los cuales se calculará la aproximación
x_values = [0, 0.5, 1, 1.5, 2]

# Número de términos de la serie de Taylor
n = 6

# Cálculo de las aproximaciones
approximations = [taylor_series_exp(x, n) for x in x_values]

# Mostrar los resultados
for x, approx in zip(x_values, approximations):
    print(f"e^{x} ≈ {approx}")

# También calculamos el valor exacto para comparar
exact_values = [math.exp(x) for x in x_values]

# Comparación entre el valor aproximado y el valor exacto
for x, approx, exact in zip(x_values, approximations, exact_values):
    print(f"x = {x}: Aproximado = {approx}, Exacto = {exact}, Error = {abs(exact - approx)}")
