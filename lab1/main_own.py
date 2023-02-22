import random


# Класс элемента списка
class Node:
    # Метод __init__ отвечает за инициализацию экземпляров класса элемента списка после их создания
    def __init__(self, data):
        self.item = data  # data - значение элемента списка
        self.nref = None  # nref - ссылка на следующий элемент списка
        self.pref = None  # pref - ссылка на предыдущий элемент списка


# Класс двусвязного списка
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None  # По умолчанию в нём нет элементов

    # Данный метод добавляет элемент в конец списка
    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)  # Создаём элемент списка
            self.start_node = new_node
            return
        n = self.start_node

        # Проходимся по всему списку
        while n.nref is not None:
            n = n.nref  # Получаем ссылку на следующий элемент последнего элемента списка

        # Вставляем новый элемент в конец списка
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    # Данный метод обходит весь список и выводит его
    def traverse_list(self):
        if self.start_node is None:
            print("Список пуст!")
            return
        else:
            n = self.start_node

            print('[', end = '')

            while n is not None:
                # Если элемент не последний отделяем его запятой
                if n.nref is not None:
                    print(n.item, end=', ')
                else:  # После последнего элемента закрываем квадратную скобку
                    print(n.item, end = ']')

                n = n.nref  # Берём следующий элемент

    # Данный метод удаляет элемент из списка по его индексу
    def delete_element_by_index(self, i):
        # Если в качестве индекса была передана строка
        if type(i) == str:
            print("Элемента с таким индексом не существует!")
            return

        n = self.start_node
        k = 0  # Переменная-счётчик общего количества элементов списка

        while n is not None:
            k += 1
            n = n.nref

        if (i < 0) or (i >= k):
            print("Элемента с таким индексом не существует!")
            return

        n = self.start_node
        k = 0

        while n is not None:
            # Если элемент с индексом i был найден
            if i == k:
                # Проверяем первый ли он
                if n.pref is None:
                    list.delete_at_start()  # Удаляем его
                    n = self.start_node  # Элемент, следующий за удалённым элементом, становится первым в списке
                    n.pref = None  # Так как он первый, то ссылки на предыдущий элемент у него не будет
                elif n.nref is None:  # Если элемент с индексом i последний
                    n.pref.nref = None  # "Забываем" его у предыдущего элемента
                else:  # Если элемент с индексом i и не первый, и не последний
                    # Аккуратненько вставляем его между двумя элементами списка
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                break
            else:  # Если элемент с индексом i не был найден
                k += 1
                n = n.nref  # Берём следующий элемент

    # Данный метод находит элемент в списке по его индексу
    def find_element_by_index(self, i):
        if type(i) == str:
            print("Элемента с таким индексом не существует!")
            return

        n = self.start_node
        k = 0

        while n is not None:
            k += 1
            n = n.nref

        if (i < 0) or (i >= k):
            print("Элемента с таким индексом не существует!")
            return

        n = self.start_node
        k = 0

        while n is not None:
            # Если элемент с индексом i был найден
            if i == k:
                return n.item  # Возвращаем его значение
                break
            else:
                k += 1
                n = n.nref

    # Данный метод удаляет первый элемент из списка
    def delete_at_start(self):
        if self.start_node is None:
            print("Список пуст!")
            return

        # Если в списке всего 1 элемент
        if self.start_node.nref is None:
            self.start_node = None
            return

        self.start_node = self.start_node.nref  # Делаем первым элементом тот элемент, который стоял после первого
        self.start_prev = None  # Ссылки на предыдущий элемент у первого элемента списка нет


a = 0  # Переменная выбора типа ввода пользователем
avrg = 0.0  # Переменная среднего арифметического чётных элементов списка
list = DoublyLinkedList()  # Создание объекта экземпляра класса кастомного списка

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
                list.insert_at_end(e)  # Кастомный метод insert_at_end добавляет элемент в конец списка

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

        list.insert_at_end(e)

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
        e = list.find_element_by_index(i)  # Кастомный метод find_element_by_index находит элемент в списке по его индексу

        if e < avrg:  # Если число по индексу i списка строго меньше среднего арифметического чётных элементов этого списка
            list.delete_element_by_index(i)  # Кастомный метод delete_element_by_index удаляет элемент из списка по его индексу
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
                list.traverse_list() # Кастомный метод traverse_list обходит весь список и выводит его

                print()

                print("Среднее арифметическое чётных элементов списка:", avrg)

                list = listUpdate(n)

                print("Список после преобразования:")
                list.traverse_list()
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
                            list.traverse_list()

                            print()

                            print("Среднее арифметическое чётных элементов списка:", avrg)

                            list = listUpdate(n)

                            print("Список после преобразования:")
                            list.traverse_list()
                            break
                break