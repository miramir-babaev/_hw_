list_1 = [9, 49, 25, 22, -1, 32, 15, 8, 2, 0, 7, 11, -9, 63, 18, 8, 0, -1, 5, 7]
list_2 = []
max = int(input('Введите максимум => '))
min = int(input('Введите минимум => '))
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')