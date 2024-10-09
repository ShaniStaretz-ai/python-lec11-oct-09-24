# targil -- use any/all
# check if a list [True, False, False, True] contains at least 1 False
#   if yes -- print '1+ False' else print '0 False'
# check if a list [False, False, False, False] contains all False
#   if yes -- print 'All False' else print 'not All False'
# *Bonus: check if a list [3, 9, 12, 15, 16] contains only numbers divided by 3 no reminder
#   if yes -- print 'All 3 divided' else print 'not All3 divided'
if not all([True, False, False, True]):#not all True
    print('1+ False')
else:
    print('0 False')
if not any([False, False, False, False]):#  not any True
    print("all False")
else:
    print('not all False')
#
# l = [3, 9, 12, 15, 16]
# l2 = [x % 3 == 0 for x in [3, 9, 12, 15, 16]]
print(all([x % 3 == 0 for x in [3, 9, 12, 15, 16]]))


bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
print('all bool1', bool1, all(bool1))  # True
print('all bool2', bool2, all(bool2))  # False
print('all bool3', bool3, all(bool3))  # False

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
bool4: list[bool] = [False, False]
bool5: list[int] = [0, 0, 0, 0, 0]
print('any bool1', bool1, any(bool1))  # True
print('any bool2', bool2, any(bool2))  # True
print('any bool3', bool3, any(bool3))  # True
print('any bool4', bool4, any(bool4))  # False
print('any bool5', bool5, any(bool5))  # False
