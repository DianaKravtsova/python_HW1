n = int(input("Сколько элементов последовательности?\n"))

a = 1
x = 1
b = 0
while x < n:

    for i in range (0, a, 1):
        if b < n:
            print(a)
            b+=1

    x += 1
    a += 1