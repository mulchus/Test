
# Поверхностное копирование и глубокое копирование
# Копирование объектов может быть выполнено как «поверхностное» (shallow) копирование или «глубокое» (deep) копирование.
# Различия между ними заключаются в том, как обрабатываются вложенные объекты.
# При поверхностном копировании создается новый объект, но его внутренние элементы (если они тоже являются объектами)
# остаются ссылками на те же объекты, что и в оригинале. Другими словами, копируются только ссылки на объекты,
# но не сами объекты.
# Заметьте, что изменения во вложенных объектах будут видны как в оригинале, так и в его поверхностной копии.
import copy

original_list = [1, 2, [3, 4]]

shallow_copied_list = copy.copy(original_list)

print(original_list)
print(shallow_copied_list)

print(original_list is shallow_copied_list)
print(original_list[2] is shallow_copied_list[2])

original_list[2] = [5, 6]
shallow_copied_list[2] = [5, 6]
print(original_list)
print(shallow_copied_list)
print(original_list[2] is shallow_copied_list[2])

deep_copied_list = copy.deepcopy(original_list)

print(original_list)
print(deep_copied_list)

print(original_list is deep_copied_list)
print(original_list[2] is deep_copied_list[2])
