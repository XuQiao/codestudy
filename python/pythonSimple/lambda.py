def make_repeater(n):
    return lambda s:s*n

twice = make_repeater(3)

print(twice('word'))
print(twice(4))

