
# ошибка использования изменяемых объектов в параметрах

while True:
    var = input('Вар 1 или 2? ')

    match var:
        case '1':
            def do_something(l=[0, 1, 2]):
                l.append(len(l))
                return l

        case '2':
            def do_something(l = None):
                if l is None:
                    l = [0,1,2]
                l.append(len(l))
                return l

    x = do_something()
    y = do_something()
    z = do_something()
    result = do_something()
    print(x, y, z, result)
