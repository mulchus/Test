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
    