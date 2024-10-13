#source:https://rt-ed.co.il/articles/python-language-questions-and-answers/
from random import randint

# from statistics import mean
#
# ex1:
# שאלה 1: כתבו תוכנית שקולטת מספרים מהמשתמש עד שנקלט התו q. הדפס את ממוצע המספרים.
# numbers: list[int] = []
# number_str = ''
# while True:
#     try:
#         number_str: str = input("enter number, if you want to stop, enter 'q':")
#         number: int = int(number_str)
#         numbers.append(number)
#     except ValueError as e:
#         if number_str == 'q':
#             print("you entered quit char ")
#             break
# if numbers:
#     print("the mean is:", mean(numbers))
#
# ex2
# # שאלה 2: כתבו תכנית בשפת פייתון שמקבלת רשימה של מספרים, ומספר נוסף. הפונקציה תשנה את הרשימה עצמה (IN-PLACE) כך שהיא לא תכיל מספרים שמתחלקים במספר הנוסף.
# l1: list[int] = [randint(1, 101) for _ in range(10)]
# print("before:", l1)
# number: int = int(input("enter number:"))
# l1 = [x for x in l1 if x % number != 0]
# print("after:", l1)
#
# ex3
# # שאלה 3: כתבו קוד בפייתון שקולטת מחרוזת מהמשתמש ומדפיסה האם היא פלינדרום (מחרזות היא פלינדרום אם היא זהה להיפוכה. למשל level, noon ו-racecar הן מילים פלינדרומיות.
# string1:str = input("enter philandrom word:")
# for i in range(len(string1)):
#     if string1[i] != string1[len(string1) - 1 - i]:
#         print("not Palindrome")
#         break;
# else:print("Palindrome")

# ex4
# שאלה 4: כתבו תכנית המדמה הגרלה. נקלוט מהמשתמש 3 מספרים שונים בין 0 ל-9. לאחר מכן התכנית תבחר באקראי 3 מספרים שונים מטווח זה (0-9). אם המספרים שנבחרו זהים לאלו שהמשתמש ניחש נדפיס "You Win" אחרת נדפיס "You Lose".
# l2_user = []
# for _ in range(3):
#     while len(l2_user) != 3:
#         x: int = int(input("enter number between 0-9:"))
#         if not 0 < x < 9:
#             print("try again")
#             continue;
#         l2_user.append(x)
# print("your selection:", l2_user)
# l3_random = [randint(0, 9) for _ in range(3)]
# print("random selection:", l3_random)
# if l2_user == l3_random:  # sum(l2_user) == sum(l3_random)
#     print("you win")
# else:
#     print("you lose")
