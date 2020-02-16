stroka = input("Введите числа через пробел\n")

lstlst = stroka.split(' ')

xx = input("Введите искомое число\n")

arr = []

for i in range(len(lstlst)):
    if lstlst[i] == xx:
        arr.append(i)

if len(arr) == 0:
    print("Отсутствует")
else:
    print(arr)
