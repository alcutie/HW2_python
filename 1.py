# ввод числа
num = int(input())
# применяем цикл для того, чтобы перебрать любое число, отличное от 1, но прибавляем +1, чтобы num включалось
for i in range(2, num + 1):
    # если число делится без остатка (остаток равен 0), то это делитель, а значит выводим его
    if num % i == 0:
        print(i)
        # т.к. нам нужен наименьший делитель, то выводим его и сразу же "станавливаем" наш цикл
        break
