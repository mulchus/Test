from attrs import asdict, define, make_class, Factory
# attrs - библиотека, которая снимает рутину при написании классов и автоматически реализует «ду́ндер»-методы
# (__init__, __repr__, __eq__ и др.).


@define
class SomeClass:
    a_number: int = 42
    list_of_numbers: list[int] = Factory(list)

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number

some_class = SomeClass(1, [1, 2, 3])
print(some_class)                     # SomeClass(a_number=1, list_of_numbers=[1, 2, 3])
print(some_class.hard_math(3))        # 19
print(asdict(some_class))             # {'a_number', 'list_of_numbers': [1, 2, 3]}
print()

print(another_class := SomeClass())         # SomeClass(a_number=42, list_of_numbers=[])
another_class.a_number = 5
another_class.list_of_numbers.extend([10, 20])
print(another_class)                    # SomeClass(a_number=5, list_of_numbers=[10, 20])
print(another_class.hard_math(2))        # 65
print(asdict(another_class))             # {'a_number', 'list_of_numbers': [1, 2, 3]}
