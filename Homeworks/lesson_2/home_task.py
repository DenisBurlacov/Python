# hals = int(input("Enter your hals: "))
# if hals <= 0:
#     print("False")
# else:
#     print("True")

# num = int(input("Enter your number: "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# year = int(input("Enter your year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Високосный')
#         else:
#             print('Невисокосный')
#     else:
#         print('Високосный')
# else:
#     print('Невисокосный')

# if not year%4 and year%100 or not year%400:
#     print('Високосный')
# else:
#     print('Невисокосный')
text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
for i in range(1, num+1):
    print(i, text)