# -*- coding: utf-8 -*-
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir símbolos
t, n = sp.symbols('t n', real=True)
T = 3
w0 = 2 * sp.pi / T

# Definir x(t) en el intervalo [-1, 1]
x_t = t + 1

# Calcular c_n (forma exponencial compleja  de Fourier)
cn = (1 / T) * sp.integrate(x_t * sp.exp(-sp.I * n * w0 * t), (t, -1, 1))
cn_simplified = sp.simplify(cn)

# Mostrar la expresión simbólica
print("c_n =", cn_simplified)

# Crear una función evaluable
cn_func = sp.lambdify(n, cn_simplified, modules='numpy')

# Evaluar para varios valores de n
n_vals = np.arange(-30, 31) #indice armonico 
c_vals = cn_func(n_vals)

# Obtener magnitudes
magnitudes = np.abs(c_vals)

# Graficar 
plt.figure(figsize=(10, 6))
markerline, stemlines, baseline = plt.stem(n_vals, magnitudes, basefmt=" ")
plt.setp(markerline, color='red', marker='o', markersize=6)
plt.setp(stemlines, color='blue', linewidth=1)
plt.title("Espectro de magnitud de $c_n$ (Serie de Fourier exponencial)")
plt.xlabel("n")
plt.ylabel("$|c_n|$")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Guardar con alta resolución
plt.savefig("espectro_cn_alta_calidad.png", dpi=1200)

# Mostrar la figura
plt.show()
