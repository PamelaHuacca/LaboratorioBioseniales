import numpy as np 

"""Creaación de vectores:a = [3.1,1, -0.5, -3.2, 6], b= [1, 3, 2.2, 5.1, 1]"""
a=np.array([[3.1,1,-0.5,-3.2,6]])
b=np.array([[1,3,2.2,5.1,1]])
"producto"
#escalar de los vectores,deben tener la misma dimensión 
dimensionA=a.shape
dimensionB=b.shape
productoEscalar=np.dot(a*b) 
print(productoEscalar)
#punto a punto 
productoPunto=a*b
print(productoPunto)

"Construir una matriz y obtener su transpuesta "
A = np.array([
    [2,   -1,   -3],
    [4,    1.5, -2.5],
    [7.3, -0.9,  0.2]
])
transpuesta= A.T
print("La tranpuesta de la Matriz A es:" ,transpuesta)

import numpy as np

# Construcción de la matriz A
A = np.array([
    [2,   -1,   -3],
    [4,    1.5, -2.5],
    [7.3, -0.9,  0.2]
])
print("Matriz  A:",A )

"Sub_matrices de Numpy "
#np.ones() -Crea una matriz de unos 
matriz_unos = np.ones(A.shape)
print("\nMatriz de unos con la dimensión de la matriz A:", matriz_unos)

# np.round()- Redondea los valores de A a 1 decimal
A_round = np.round(A, 1)
print("Matriz A redondeada a 1 decimal:", A_round)

# np.ceil()-Redondea hacia arriba
A_ceil = np.ceil(A)
print("Matriz A redondeada hacia arriba (ceil):", A_ceil) #Redondea hacia arriba

# np.floor()- Redondea hacia abajo
A_floor = np.floor(A)
print("Matriz A redondeada hacia abajo (floor):",A_floor)

"""Acceda al valor de la primera fila, tercera columna de la matriz A, imprímalo en consola."""
valor=A[0,2]
print("El valor es :" , valor)
"""Obtenga la segunda fila de dicha matriz, imprímalo en consola."""
segunda_fila=A[1,:]
print("segunda fila es",segunda_fila)

"""comando para conocer las dimensiones de la matriz A"""
dimension_Matriz_A= A.shape
print("La dimensión de la matriz A es:", dimension_Matriz_A)