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
<<<<<<< HEAD
# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)

working_hours = int(input("Enter the working hours: "))
prise_of_hour = int(input("Enter the prise of one hour: "))


def cost_of_work(working_hours, prise_of_hours):
    result = working_hours * prise_of_hours
    return result


print("You yerned " + str(cost_of_work(working_hours, prise_of_hour)) + " " + "today !")
=======
text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
for i in range(1, num+1):
    print(i, text)
>>>>>>> origin/main
