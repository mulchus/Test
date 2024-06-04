try:
    x = 0
    # x = int(input("Введите число: "))
    y = 1 / x
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число!")
else:
    print("Результат: ", y)
finally:
    print("Конец программы")


try:
    raise TypeError('some error')
except Exception as e:
    print(e)
    print(f'I catch it into Exception = {e!r}')
    # raise FileNotFoundError  # and raise another
except TypeError as e:
    print(e)
    print(f'I catch it into TypeError = {e!r}')
    raise


try:
    # raise TypeError('some error')
    pass
except TypeError as e:
    print(f'I catch it into Exception = {e!r}')
    raise e  # and raise another
finally:
    print('finally')


# определение собственных исключений
class MyCustomException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info


try:
    raise MyCustomException("Произошла ошибка", {"code": 400, "time": "12:34"})
except MyCustomException as e:
    print(f"Сообщение об ошибке: {e}")
    print(f"Дополнительная информация: {e.extra_info}")
