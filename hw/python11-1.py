from random import choice, randint

# a
l_booleans: list[bool] = [choice([True, False]) for _ in range(3)]
print("Boolean list:", l_booleans)
# b
print("is all True:", all(l_booleans))
# c
print("is at least 1 True:", any(l_booleans))
# d
if not any(l_booleans):
    print("all False:", l_booleans)
else:
    print("not all False:", l_booleans)
# e
if not all(l_booleans):
    print("at least 1 False:", l_booleans)
else:
    print("not at least 1 True:", l_booleans)

# f
l_rand_two: list[int] = [randint(-2, 2) for _ in range(5)]
print("random [-2:2] list:", l_rand_two)
# g
print("is all not zero:", all([x != 0 for x in l_rand_two]))
# h
print("at least 1 not zero:", any([x != 0 for x in l_rand_two]))
# i
print("all zero:", all([x == 0 for x in l_rand_two]))
# j
print("at least 1 zero:", any([x == 0 for x in l_rand_two]))
