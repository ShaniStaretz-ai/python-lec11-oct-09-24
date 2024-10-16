from random import choice, randint

# a
l_booleans: list[bool] = [choice([True, False]) for _ in range(3)]
print("Boolean list:", l_booleans)
# b
print("is all True:", all(l_booleans))
# c
print("is at least 1 True:", any(l_booleans))
# d
print("is all False:", not any(l_booleans))
# e
print("is at least 1 False:", not all(l_booleans))

# f
l_rand_two: list[int] = [randint(-2, 2) for _ in range(5)]
print("random [-2:2] list:", l_rand_two)
# g
# print("is all not zero:", all(l_rand_two))
print("is all not zero:", all([x != 0 for x in l_rand_two]))
# h
# print("is all not zero:", any(l_rand_two))
print("is at least 1 not zero:", any([x != 0 for x in l_rand_two]))
# i
print("is all zero:", not any(l_rand_two))
print("is all zero:", all([x == 0 for x in l_rand_two]))
# j
print("is at least 1 zero:", not all(l_rand_two))
print("is at least 1 zero:", any([x == 0 for x in l_rand_two]))
# first option is better because without addition list
# first option is correct only because the values can be zero
