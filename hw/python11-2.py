me: str = "Shani Staretz Kfar Saba"
# a
print("size:", len(me))
# b
print("upper:", me.upper())
# c
print("lower:", me.lower())
# d
print("is startswith 'Shani':", me.startswith("Shani"))
# e
print("is endswith 'Kfar Saba':", me.endswith("Kfar Saba"))
# f
print("split:", me.split(" "))
# g
print("split:", me.replace(' ', '*').split("*"))
# h
print("center:", me.center(50, '='))
# i
print("4-end:", me[3:])  # including the 4 char
# j
print("start-4:", me[:4])  # including the 4 char
# k
print("even chars:", me[1::2])  # evens from second char
# l
print("title:", me.title())  # including the 4 char
