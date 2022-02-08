# класс стека, для создания 2-х объектов, стек операций, стек чисел и переменных
class stack:
    def __init__(self, mass):
        self.obj_stack = []
        for el in mass:
            self.add_obj(el)

    def add_obj(self, obj):
        self.obj_stack = [obj] + self.obj_stack

    def delete(self):
        head, *self.obj_stack = self.obj_stack
        return head

    def show_stack(self):
        for i in range(len(self.obj_stack)):
            print(self.obj_stack[i], end=' ')

    def checking_empty(self):
        if len(self.obj_stack) == 0:
            return True
        else:
            return False

    def return_head(self):
        if len(self.obj_stack) != 0:
            return self.obj_stack[0]
        else:
            return -1

    def delete_couple_of_first(self):
        first_el, second_el, *self.obj_stack = self.obj_stack
        return second_el, first_el

    def return_len(self):
        return len(self.obj_stack)

    def return_stack(self):
        return self.obj_stack


# создание объектов класса стек
operations_stack = stack([])
other_stack = stack([])
# ввод значения k
while True:
    print("Введите значение k -> ", end=' ')
    k = input()
    if k.isdigit():
        if 1 < int(k) < 6:
            k = int(k)
            break
        else:
            print("Некорректное значение k...")
    else:
        print("Некорректное значение k...")

# списки значений переменных - аналог таблицы значений
x_pattern = []
y_pattern = []
op_list = ['(', ')', '+', '^']  # список операций, нужен для проверки во время обхода

# ввод значения n
while True:
    print("Введите значение n -> ", end=' ')
    n = input()
    if n.isdigit():
        if int(n) != 1 and int(n) != 2:
            print("Некорректное значение n...")
        else:
            n = int(n)
            break
    else:
        print("Некорректное значение n...")

# в зависимости от того, сколько у нас переменных, по-разному заполняем списки значений x или x,y
if n == 2:
    for i in range(k):
        for j in range(k):
            x_pattern.append(i)
            y_pattern.append(j)

else:
    for i in range(k):
        x_pattern.append(i)


# функция операции сложения по модулю k
def op_plus(x, y, n):
    res = []
    # в зависимости от кол-ва переменных возвращаем списки разных размерностей
    if n == 2:
        for i in range(k * k):
            res.append(0)
        for i in range(len(x)):
            res[i] = (x[i] + y[i]) % k
    else:
        for i in range(k):
            res.append(0)
        for i in range(len(x)):
            res[i] = (x[i] + y[i]) % k
    return res


# функция операции возведения в степень 3
def op_step(x, n):
    res = []
    # в зависимости от кол-ва переменных возвращаем списки разных размерностей
    if n == 2:
        for i in range(k * k):
            res.append(0)
        for i in range(len(x)):
            res[i] = (x[i] * x[i] * x[i]) % k
    else:
        for i in range(k):
            res.append(0)
        for i in range(len(x)):
            res[i] = (x[i] * x[i] * x[i]) % k
    return res


def take(ch, n):  # 'выдергиватель' переменных из стека
    if ch <= 0:  # если переменных две
        first = other_stack.delete()  # 1 и 2  переменная
        second = other_stack.delete()
        if first == 'x':  # если переменная все еще строка, переделываем в список значений
            first = x_pattern
        elif first == 'y':
            first = y_pattern
        elif str(type(first)) == "<class 'list'>":  # если уже список, ничего не делаем
            pass
        else:
            first = int(first)  # если переменная, то делаем ее целочисленной
        if second == 'x':  # аналогично со 2 переменной
            second = x_pattern
        elif second == 'y':
            second = y_pattern
        elif str(type(second)) == "<class 'list'>":
            pass
        else:
            second = int(second)

        if str(type(first)) == "<class 'int'>":  # если обе константы
            if str(type(second)) == "<class 'int'>":
                first_num = first
                sec_num = second
                first = []
                second = []
                if n == 2:
                    for i in range(k * k):
                        first.append(first_num)
                        second.append(sec_num)
                else:
                    for i in range(k):
                        first.append(first_num)
                        second.append(sec_num)
            else:
                first_num = first
                first = []
                if n == 2:
                    for i in range(k * k):
                        first.append(first_num)
                else:
                    for i in range(k):
                        first.append(first_num)
        elif str(type(second)) == "<class 'int'>":
            sec_num = second
            second = []
            if n == 2:
                for i in range(k * k):
                    second.append(sec_num)
            else:
                for i in range(k):
                    second.append(sec_num)
        res = []
        res.append(first)
        res.append(second)
        return res  # возвращаем список значений
    else:  # если всего одна переменная
        one = other_stack.delete()
        if one == 'x':
            one = x_pattern
        elif one == 'y':
            one = y_pattern
        elif str(type(one)) == "<class 'list'>":
            pass
        else:
            one = int(one)

        if str(type(one)) == "<class 'int'>":
            one_num = one
            one = []
            if n == 2:
                for i in range(k * k):
                    one.append(one_num)
            else:
                for i in range(k):
                    one.append(one_num)
        res = []
        res.append(one)
        return one


def blues(mass):  # функция нахождения СКНФ
    res = ''  # сюда будет записан результат
    x_count = 0  # для записи вида J0(x) и т.д.
    y_count = 0
    if n == 2:
        for i in range(len(mass)):
            if mass[i] == k - 1:
                pass
            else:
                if mass[i] != 0:
                    res = res + '&(' + str(mass[i]) + 'v~J' + str(x_count) + '(x)v~J' + str(y_count) + '(y))'
                else:
                    res = res + '&(' + '~J' + str(x_count) + '(x)v~J' + str(y_count) + '(y))'

            y_count += 1
            if y_count == k:
                x_count += 1
                y_count = 0
    else:
        for i in range(len(mass)):
            if mass[i] == k - 1:
                pass
            else:
                if mass[i] != 0:
                    res = res + '&(' + str(mass[i]) + 'v~J' + str(x_count) + '(x))'
                else:
                    res = res + '&' + '~J' + str(x_count) + '(x)'

            x_count += 1
    return res[1:]  # возвращаем результат


# функция определения принадлжености к множеству
def T_master(T, ans):
    T = T.split()
    for i in range(len(T)):  # обработка введенного мн-ва
        if not T[i].isdigit():
            continue
        T[i] = int(T[i])
    if n == 1:
        for i in range(k):
            f = ans.pop(0)  # берем значения функции из таблицы, которую передали аргументом
            if i in T:
                if f in T:
                    checkin = 1
                else:
                    checkin = 0
                    break
    elif n == 2:
        for i in range(k):
            for j in range(k):
                f = ans.pop(0)
                if i in T and j in T:
                    if f in T:
                        checkin = 1
                    else:
                        checkin = 0
                        break
    if checkin == 1:  # если принадлежит мн-ву
        s = ''
        for i in T:
            s += str(i) + ', '
            s = s[:len(s) - 2]
        print('f принадлежит T {' + s + '}')
    else:  # иначе
        s = ''
        for i in T:
            s += str(i) + ', '
        s = s[:len(s) - 2]
        print('f не принадлежит T {' + s + '}')


# функция считывания функции
def wizzard(st):
    i = 0
    end_i = len(st)
    skob_c = 0
    while i < end_i:
        if st[i] == '/':  # если дошли до конца
            if operations_stack.return_head() == '+':  # если вершина стека операций +
                result = take(0, n)  # считываем две переменные или константы из стека переменных
                other_stack.add_obj(
                    op_plus(result[0], result[1], n))  # и вызываем функцию операции + и добавляем результат в стек
            elif operations_stack.return_head() == '^':  # аналогично со степенью
                result = take(1, n)
                other_stack.add_obj(op_step(result, n))
            else:
                other_stack.add_obj(take(1, n))  # в случае, если мы ввели одну переменную или константу (в таком случае стек операций будет пуст) просто переделываем ее в список значений и возвращаем в стек переменных
            break
        if st[i] not in op_list:  # если символ не операция
            other_stack.add_obj(st[i])  # добавляем в стек переменных
            i += 1
        elif st[i] == '+':  # если операция сложения
            if operations_stack.return_head() == '+':  # и это сложение
                result = take(0, n)  # берем из стека переменных 2 переменные
                other_stack.add_obj(
                    op_plus(result[0], result[1], n))  # производим вычисления и добавляем список значений в стек
                i += 1
            else:
                operations_stack.add_obj(st[i])
                i += 1
        elif st[i] == '^':  # аналогично со степенью
            result = take(1, n)
            other_stack.add_obj(op_step(result, n))
            i += 2  # т.к. мы возводим в степень константы (3), будет легче проходить сразу два символа
        elif st[i] == '(':  # если мы встречаем (, то просто добавляем ее в стек операций
            operations_stack.add_obj(st[i])
            i += 1
        elif st[i] == ')':  # встречаем закрывающуюся скобку )
            if operations_stack.return_head() == '(':  # если мы сразу после ее мы встречаем (, значит у нас записано что-то по типу (x)
                operations_stack.delete()  # убираем (
                i += 1  # идем дальше
            else:
                while operations_stack.return_head() != '(':  # иначе мы должны вычислить все, что между скобками, т.е. все операции до первой попавшийся (
                    op = operations_stack.delete()

                    if op == '+':  # я не рассматриваю случай со степенью, т.к. имеется два варианта -> x^3 и в этом случае вычисления происходят сразу же, (...)^3 , тут сначала вычисляется все в скобке и после этот случай превращается в первый случай
                        result = take(0, n)
                        other_stack.add_obj(op_plus(result[0], result[1], n))
                operations_stack.delete()
                i += 1


while True:  # меню
    print("[МЕНЮ]")
    print("Доступные функции -> 1. x + y")
    print("                  -> 2. x^3")
    print("Введите функцию -> ", end='')
    func = input()
    func += '/'  # добавляем лишний символ, чтобы легче было обрабатывать строку
    if n == 1:
        if 'y' in func:  # лишняя переменная, т.к. не пойдет
            break

    wizzard(func)  # вызываем функцию считывания строки
    ans = other_stack.return_head()  # после в стеке переменных у нас останется один элемент, он и будет результатом
    if n == 1:  # вывод таблицы
        print("   x    f(x) ")
        for i in range(len(ans)):
            print("| ", i, " | ", ans[i], " |")
    elif n == 2:
        x_count = 0
        y_count = 0
        print("  x   y   f(x)")
        for i in range(len(ans)):
            print("|", x_count, "|", y_count, "| ", ans[i], " |")
            y_count += 1
            if y_count == k:
                x_count += 1
                y_count = 0

    print("Аналог СКНФ -> ", end='')
    print(blues(other_stack.return_head()))  # вызываем функцию, которая возвращает аналог СКНФ

    T = str(input('Введите множество чисел через пробел: '))
    T_master(T, ans.copy())  # проверка на принадлежность мн-ву

    break  # конец работы программы
    '''АЛГОРИТМ'''
    '''ВЫВОД'''
