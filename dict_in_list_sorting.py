employees = [
    {"name": "Alice", "age": 30, "salary": 70000},
    {"name": "Bob", "age": 25, "salary": 150000},
    {"name": "Charlie", "age": 35, "salary": 120000}
]

# Сортировка по возрасту
sorted_employees = sorted(employees, key=lambda x: x["age"])
print(sorted_employees)


# Сортировка по зарплате
employees.sort(key=lambda x: x["salary"])
print(employees)


# Сортировка по возрасту в обратном порядке
sorted_employees_desc = sorted(employees, key=lambda x: x["age"], reverse=True)
print(sorted_employees_desc)


# Использование функции `itemgetter` из модуля `operator`
# Это более эффективный способ, чем лямбда-функция, особенно для больших данных.
from operator import itemgetter
sorted_employees = sorted(employees, key=itemgetter("age"))
print(sorted_employees)


# Обработка отсутствующих значений
# Если поле может отсутствовать в некоторых словарях, можно использовать параметр key для обработки таких ситуаций.
employees = [
    {"name": "Alice", "age": 30},
    {"name": "Bob"},
    {"name": "Charlie", "age": 35}
]
sorted_employees = sorted(employees, key=lambda x: x.get("age", 0))
print(sorted_employees)
