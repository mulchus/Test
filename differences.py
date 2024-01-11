
# использовать get_close_matches() из модуля difflib, чтобы вернуть список лучших  совпадений.
from difflib import get_close_matches

names = ['julian', 'pybites', 'bob', 'tlm', 'python', 'sara', 'james', 'ana']

print(get_close_matches('pythonista', names))
print(get_close_matches('pybit', names))
print(get_close_matches('jul', names))
print(get_close_matches('ara', names))
