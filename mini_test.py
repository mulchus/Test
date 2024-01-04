from collections import namedtuple

Parts = {'id': 10, 'desc': 'Ford', 'cost': 2000.0, 'amount': 30}
print(Parts.__contains__('amount'))

parts = namedtuple('Parts', Parts.keys())(**Parts)

print(parts.amount)
