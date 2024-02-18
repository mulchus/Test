try:
    raise TypeError('some error')
except Exception as e:
    print(e)
    print(f'I catch it into Exception = {e!r}')
    raise   # and raise another
except TypeError as e:
    print(e)
    print(f'I catch it into TypeError = {e!r}')
    