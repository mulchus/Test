from operator import itemgetter

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
f = itemgetter(4, 6)
print(f(days))

workouts = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
print(itemgetter('Mon', 'Wed')(workouts))
