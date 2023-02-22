import random


a = 0  # Переменная выбора типа ввода пользователем
avrg = 0.0  # Переменная среднего арифметического чётных элементов списка
list = []


# Метод пользовательского ввода с обработкой всех исключений
def userInput():
    while True:
        try:
            a = int(input("Пожалуйста выберите, каким образом вы хотели бы заполнить список: вручную (введите 0) или автоматически случайными "
        "числами (введите 1): "))
        except ValueError:
            print("Пожалуйста введите целое число из предложенных вариантов")
        else:
            if ((a != 0) and (a != 1)):
                print("Пожалуйста введите целое число из предложенных вариантов")
            else:
                return a
                break


# Метод ручного заполнения списка пользователем с обработкой всех исключений
def listUserInput(avrg):
    k = 0  # Переменная-счётчик количества чётных элементов списка

    for i in range(n):
        while True:
            try:
                e = float(input())  # float используется для универсальности
            except ValueError:
                print("Пожалуйста введите число")
            else:
                list.append(e)  # Метод append добавляет элемент в конец списка

                if (e % 2) == 0:  # Если введённое пользователем число e чётное
                    avrg += e  # Суммируем его в переменную среднего арифметического
                    k += 1
                break

    if k != 0:
        avrg /= k

    return avrg


# Метод автоматического заполнения списка случайными числами
def listRandomInput(avrg):
    k = 0

    for i in range(n):
        # Метод randint генерирует случайное целое число в диапазоне от l до r, введённом пользователем с обработкой всех исключений
        e = random.randint(l, r)

        list.append(e)

        if (e % 2) == 0:
            avrg += e
            k += 1

    if k != 0:
        avrg /= k

    return avrg


# Метод для удаления элементов списка, меньших среднего арифметического чётных элементов этого списка
def listUpdate(n):
    i = 0

    while i < n:  # Проходимся по всем индексам элементов списка
        if list[i] < avrg:  # Если число по индексу i списка строго меньше среднего арифметического чётных элементов этого списка
            list.pop(i)  # Метод pop удаляет i-ый элемент из списка
            n -= 1  # Уменьшаем размер списка n на 1 только что удалённый элемент

            if i > 0:
                # После удаления из списка элемента, его место займёт элемент, который до его удаления стоял перед ним.
                # Чтобы рассмотреть этот элемент, необходимо вернуться на 1 индекс назад (-1) кроме случая, когда мы удалили
                # из списка первый элемент с индексом 0 (элемента с индексом -1 не существует)
                i -= 1
        else:
            i += 1  # Иначе идём дальше (+1) по циклу и берём индекс следующего элемента списка

    return list


a = userInput()

if a == 0:  # Если пользователь выбрал ручной ввод
    while True:
        try:
            n = int(input("Пожалуйста введите количество элементов списка: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (n <= 0):
                print("Пожалуйста введите целое положительное число")
            else:
                print("Пожалуйста введите элементы списка: ")

                avrg = listUserInput(avrg)

                print("Список до преобразования:")
                print(list)

                print("Среднее арифметическое чётных элементов списка:", avrg)

                list = listUpdate(n)

                print("Список после преобразования:")
                print(list)
                break
else:  # Если пользователь выбрал автоматический (случайный) ввод
    while True:
        try:
            n = int(input("Пожалуйста введите количество элементов списка: "))
        except ValueError:
            print("Пожалуйста введите целое положительное число")
        else:
            if (n <= 0):
                print("Пожалуйста введите целое положительное число")
            else:
                while True:
                    try:
                        l = int(input("Пожалуйста введите значение левой границы диапазона для генерации случайных чисел: "))
                        r = int(input("Пожалуйста введите значение правой границы диапазона для генерации случайных чисел: "))
                    except ValueError:
                        print("Пожалуйста введите целое число")
                    else:
                        if l > r:
                            print("Левая граница диапазона для генерации случайных чисел должна быть меньше или равна правой!")
                        else:
                            avrg = listRandomInput(avrg)

                            print("Список до преобразования:")
                            print(list)

                            print("Среднее арифметическое чётных элементов списка:", avrg)

                            list = listUpdate(n)

                            print("Список после преобразования:")
                            print(list)
                            break
                break