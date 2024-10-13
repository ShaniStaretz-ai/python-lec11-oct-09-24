# a
print("strip:" + " fun-day ".strip())
# b
print("is all alphas:", "hello".isalpha())
# c
print("is all digits:", "777".isdigit())
# d
print("is all spaces:", "  ".isspace())
# e
print("join:", ''.join(['N', 'I', 'N', 'J', 'A']))
# f
print("join *:", '*'.join(['N', 'I', 'N', 'J', 'A']))
# g
print("is e in hELLo:", 'e'.lower() in 'hELLo'.lower())
# h
print([l.upper() for l in input("Enter word:") if l.isalpha()])
