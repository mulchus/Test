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
# print(sum(m, ''))   # TypeError: sum() can't sum strings [use ''.join(seq) instead]

# фильтрация списка в Python, на примере функции filter - нечетные
nums = [11, 22, 31, 42, 51]

def is_num_odd(z):
  return z % 2 != 0

out_nums = filter(is_num_odd, nums)
out_nums = list(out_nums)
print(out_nums) # -> [11, 31, 51]

Остальные методы фильтрации и их сравнение можно увидеть в статье - https://techbeamers.com/how-do-you-filter-a-list-in-python/



