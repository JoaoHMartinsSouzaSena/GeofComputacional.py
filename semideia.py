def f(x):
    return x**3 - x**2 - x - 1
    
delta_x = 0.1
x = 0

derivada = (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)
derivada_real = ((3*x**2) - (2*x) - 1)

derivada_segunda = (f(x + delta_x) - 2*f(x) + f(x - delta_x)) / (delta_x**2)
derivada_segunda_real = ((6*x) - 2)

print(f"derivada: {derivada:.6f}")
print(f"derivada real: {derivada_real:.6f}")
print(f"Segunda derivada numérica: {derivada_segunda:.6f}")
print(f"Segunda derivada real: {derivada_segunda_real:.6f}")
