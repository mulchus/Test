#  https://docs.python.org/3.11/library/shlex.html
import shlex
s = 'Поистине можно сказать, что "мой опыт" находится в "полном согласии" с нашими выводами об эволюции.'
print(s)
print(shlex.quote(s))
print(s.split())
s_shlexs = shlex.split(s)
print(shlex.join([*s_shlexs]))
print(f'{s_shlexs}', end='\n\n')

# without shlex
import re
s_re = [element.strip('"') for element in re.findall(r'"[^"]*"|[^"\W]+', s)]
print(s_re)

# sum some iter of lists
l=[['a', 'b', 'c'], ['1', '2'], ['#']]
print(sum(l, []))

m = ['1', '2', '3']
print(sum(m, ''))   # TypeError: sum() can't sum strings [use ''.join(seq) instead]
