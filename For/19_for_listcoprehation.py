a, b = (int(i) for i in input().split())  #list comprehension
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)
