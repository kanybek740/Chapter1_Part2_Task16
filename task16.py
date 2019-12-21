age = int(input())
if age % 2 == 0:
    for i in range(2, age + 1, 2):
        print(i, end=' ')

else:
    for i in range(1, age + 1,2):
        print(i, end=' ')