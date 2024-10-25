import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту A - (Лимонад)
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість продукту B -(Фруктовий сік)

# Функція цілі (Максимізація прибутку)
model += A + B, "Profit"

# Додавання обмежень
model += 2 * A + 1 * B <= 100   # Обмеження по ресурсу 1 - (Вода)
model += 1 * A <= 50  # Обмеження по ресурсу 2 - (Цукор)
model += 1 * A <= 30  # Обмеження по ресурсу 3 - (Лимонний сік)
model += 2 * B <= 40  # Обмеження по ресурсу 4 - (Фруктове пюре)

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Оптимальна кількість Лимонаду:", A.varValue)
print("Оптимальна кількість Фруктового соку:", B.varValue)
print("Максимальна загальна кількість продуктів:", pulp.value(model.objective))