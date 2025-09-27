import numpy
# 1
def number_var_ave(lists):
    num = 0
    for i in lists:
        lists[num] = int(i)
        num += 1
    ave = numpy.average(lists)
    var = numpy.var(lists)

    print(f"Среднее арифметическое: {ave}\nДисперсия: {var}")

lists = str.split(input("Пишите значения через , и пробел: "), ", ")


number_var_ave(lists)

# 2
def count_inform(count_alph, count_line, count_symb_per_line):
    syc = 0
    while True:
        if 2 ** syc < count_alph:
            syc += 1
        else:
            break
    inf_per_symb = 2 ** syc
    print(f"Вам понадобится {inf_per_symb * count_symb_per_line * count_line * 2} байт")

count_inform(int(input("Кол-во букв в алфавите: ")), int(input("Кол-во строк: ")), int(input("Кол-во символов в строке: ")))

# 3

def correct_date(year, month, day):
    if year % 4 != 0:
        if month < 13 and month > 0:
            can_day = [31,28,31,30,31,30,31,31,30,31,30,31]
            if day < can_day[month - 1] + 1 and day > 0:
                return "Дата существует"
            else:
                return "Дата не существует"
        else:
            return "Дата не существует"
    else:
        if month < 13 and month > 0:
            can_day = [31,29,31,30,31,30,31,31,30,31,30,31]
            if day < can_day[month - 1] + 1 and day > 0:
                return "Дата существует"
            else:
                return "Дата не существует"
        else:
            return "Дата не существует"

print("Введите дату. \nПример 09.05.2025")
correct_date(int(input("Введите год: ")), int(input("Введите месяц: ")), int(input("Введите день: ")))


