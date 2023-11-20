pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


def key(a: list, b: int):
    """Do nothing, but document it.

    bla-bla-bla       ,
    No, really, it doesn't do anything.
    """
    for i in a:
        print(i[b], end=', ')


print(key.__doc__)
print(key.__annotations__)

print(key(pairs, 0))

pairs.sort(key=key(pairs, 0))

print('\n', pairs)


def ch(pairs):
    return lambda x: x + pairs[1]


print(ch(pairs))

pairs = [1, 5, 3, 8]
pairs.sort(reverse=True)
print(pairs)

print((1, 'one')[1])


exit()
def func(*, kwargs):
    for let in range(0, kwargs):
        print(let)
        # print(**args)


func(kwargs=1)

exit()

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           )

exit()

def i():
    i = 5
    return i


def f(arg=i()):
    print(arg+1)


i = 6
f()

exit()




def printus(n):
    n += 2
    return n


a1 = printus(5)

print(type(printus(8)))
# print(type(a1))


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


f100 = fib2(100)    # call it
print(f100)                # write the result
