import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# 1. Обчислення інтегралу методом Монте-Карло
N = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Кількість точок, що потрапляють під криву
under_curve = y_random < f(x_random)
monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / N

# 2. Перевірка за допомогою аналітичного розрахунку та функції quad
analytical_result = (b ** 3) / 3 - (a ** 3) / 3
quad_result, quad_error = spi.quad(f, a, b)

# 3. Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Точки методу Монте-Карло
ax.scatter(x_random, y_random, color="blue", s=0.5, alpha=0.1)
ax.scatter(x_random[under_curve], y_random[under_curve], color="green", s=0.5, alpha=0.1)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Інтеграл f(x) = x^2 методом Монте-Карло та аналітично')
plt.grid()
plt.show()

# Виведення результатів
print(f"Інтеграл методом Монте-Карло: {monte_carlo_integral}")
print(f"Аналітичний інтеграл: {analytical_result}")
print(f"Інтеграл з функцією quad: {quad_result} з помилкою {quad_error}")