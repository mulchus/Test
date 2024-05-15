try:
    x = int(input("Введите число: "))
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
    raise TypeError('some error')
except TypeError as e:
    print(f'I catch it into Exception = {e!r}')
    raise e  # and raise another
finally:
    print('finally')
    