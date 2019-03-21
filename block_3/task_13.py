# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.

n = int(input())

table = {}

for i in range(n):
    temp = input().split(';')
    # Создаем ключ с командой либо добавляем +1 игру к первому элементу списка
    if temp[0] not in table:
        table[temp[0]] = [1, 0, 0, 0, 0]
    else:
        table[temp[0]][0] += 1
    if temp[2] not in table:
        table[temp[2]] = [1, 0, 0, 0, 0]
    else:
        table[temp[2]][0] += 1
    # Теперь добавляем очки
    # Победа первой
    if temp[1] > temp[3]:
        table[temp[0]][1] += 1
        table[temp[2]][3] += 1
        table[temp[0]][4] += 3
    # Победа второй
    elif temp[3] > temp[1]:
        table[temp[2]][1] += 1
        table[temp[0]][3] += 1
        table[temp[2]][4] += 3
    else:
        table[temp[0]][2] += 1
        table[temp[2]][2] += 1
        table[temp[0]][4] += 1
        table[temp[2]][4] += 1


for key,values in table.items():
    print(key,end=':')
    [print(i,end= ' ') for i in values]
    print()


def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1,
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))