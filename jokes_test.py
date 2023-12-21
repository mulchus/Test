from dataclasses import dataclass


# @dataclass
class Entity(object):
    def __init__(self, *args):
        self.health = args[0]
        self.hands = args[1]
        if args[2:]:
            self.other = args[2:]
        # health: int
        # hands: int


# @dataclass
class Human(Entity):
    pass


a = Entity(1, 2, 3, 4, 5)

b = Human(2, 11)

print(a.health, a.hands, a.other)
print(b.health, b.hands, b.other if hasattr(b, 'other') else '')


@dataclass
class Entity2:
    health: int
    hands: int
    other: tuple


@dataclass
class Human2(Entity2):
    pass


a = Entity2(10, 20, (30, 40, 50))

b = Human2(20, 110, ())

print(a.health, a.hands, a.other)
print(b.health, b.hands, b.other if hasattr(b, 'other') else '')
print(a.__dir__())

for atr in a.__dir__():
    print(f'{atr}: {a.__getattribute__(atr)}')

print(a.__dir__())
print(a.__dict__)
print(a.__hash__)


# JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES


import sys
sys.allow_boolean_assignment = 1

Тrue = False
if Тrue:
    print("Тrue is Тrue")
else:
    print("Тrue is False")


# JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES JOKES





