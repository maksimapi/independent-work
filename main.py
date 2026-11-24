import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')
w1, w2 = sp.symbols('w1 w2')

s = sp.cos(w1 * t) + sp.cos(w2 * t)

print("Сигнал:")
print(s)

print("Производная:")
print(sp.diff(s, t))

print("Интеграл:")
print(sp.integrate(s, t))


w1 = 10
w2 = 11

t = np.linspace(0, 20, 1000)

s = np.cos(w1 * t) + np.cos(w2 * t)

a = 2 * np.cos((w1 - w2) * t / 2)

plt.figure(figsize=(10, 5))

plt.plot(t, s, label='s(t)')
plt.plot(t, a, 'r--', label='Верхняя огибающая')
plt.plot(t, -a, 'g--', label='Нижняя огибающая')

plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('Биения двух близких гармоник')

plt.legend()
plt.grid()

plt.show()
