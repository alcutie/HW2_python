# первое число
first = int(input())
# в переменной maxim будет максимальное число в последовательности, изначально оно равно first
# т.к. first - единственное число в последовательности
maxim = first
# количество повторений максимального числа в последовательности
repnum = 1

# пока первое число не равно нулю
while first != 0:
    # вводим новое (второе) число
    second = int(input())
    # если второе число равно нулю, то цикл останавливается
    if second == 0:
        break
    # если второе число больше максимального на данный момент
    if second > maxim:
        # то перезаписываем значение максимального числа
        # и т.к. maxim только появился => он не мог повторится до этого
        maxim = second
        repnum = 1
    # если второе число равно максимальному
    elif second == maxim:
        # то оно повторяется, а значит прибавляем 1 к переменной с количеством повторений
        repnum += 1
    # второе число перезаписываем в переменную первого для ввода нового числа
    first = second

# выводим итоговое количество повторений максимального числа в последовательности
print(repnum)
