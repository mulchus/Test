import datetime
import decimal

name = 'mini_test'
number = 50

print(f"name={name}")
print(f"number={number}")

print(f"{name=}".replace("'", ""))
print(f"{number=}")


today = datetime.datetime.today()
print(f"{today:%Y-%m-%d}")
# 2022-03-11
print(f"{today:%Y}")
# 2022
print(f"{today:%d/%m}")
# 03/11


x = 10
print(f"{x = :.3f}")
# x = 10.000


# пример с классом
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User's name is: {self.first_name} {self.last_name}"


user = User("John", "Doe")
print(f"{user}")
# John Doe
print(f"{user!r}")
# User's name is: John Doe

text = "hello world"

# Центрирование текста:
print(f"{text:^15}")
# '  hello world  '

number = 1234567890
# Установка разделителя групп разрядов
print(f"{number:,}")
# 1,234,567,890

number = 123
# Добавление начальных нулей
print(f"{number:08}")
# 00000123

# Вложенные f-строки
number = 254.346567
print(f"{f'${number:.3f}':>10s}")
# '  $254.347'


width = 8   # Ширина строки в символах
precision = 4   # Количество знаков всего числа
value = decimal.Decimal("42.12345")
print(f"output: {value:{width}.{precision}}")
# 'output:     42.12'


# Условное форматирование !!!
value = decimal.Decimal("42.12345")
print(f'Result: {value:{"14.4" if value < 100 else "8.3"}}')
# Result:           42.12
value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.4"}}')
# Result:      142.1


print(f"{(lambda x: x**2)(3)}")
# 9

from datetime import datetime
landing = datetime(1969, 7, 20, 20, 17, 40)

landing.strftime("%a, %d %b %Y %H:%M:%S")

print(f"{landing:%a, %d %b %Y %H:%M:%S}")
