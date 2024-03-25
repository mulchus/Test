def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times_three = make_multiplier_of(3)

times_five = make_multiplier_of(5)

print(times_three(9))
print(times_five(3))
