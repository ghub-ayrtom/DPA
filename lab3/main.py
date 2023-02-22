import csv  # Библиотека импорта и экспорта для электронных таблиц и баз данных
from pathlib import Path  # Библиотека позволяет манипулировать путями файловых систем в любой операционной системе


path = input("Пожалуйста введите полный путь до папки или директорию: ")
directory = Path(path)  # Получаем объект пути до указанной папки или директории

if not directory.is_dir():  # Если полученный объект действительно является корректной директорией
    print(ValueError(f"[{directory}] не существует или не является директорией!"))
else:
    # Метод iterdir создаёт итератор, который случайным образом перечисляет файлы, не включая подпапки и поддиректории
    print(f"Только в папке (директории) [{path}] находится {len(list(directory.iterdir()))} объектов")
    # Метод rglob создаёт итератор, который случайным образом перечисляет файлы, включая подпапки и поддиректории
    print(f"В папке (директории) [{path}] и в её папках (поддиректориях) находится {len(list(directory.rglob('*')))} объектов")

print()

fI = open("C:\\Users\\Admin\\PycharmProjects\\DPA\\lab3\\data.csv", 'r')  # Открываем файл для чтения (read)
# Класс DictReader модуля csv создаёт объект, который работает как обычный reader(), но отображает информацию о каждой строке в качестве словаря dict
reader = csv.DictReader(fI, fieldnames = None, restkey = None, restval = None, dialect = "excel")

l = list(reader)  # Преобразуем его в список словарей

print("Исходные данные:\n", l)

# Сортируем список при помощи лямбда-функции по столбцу с полом из таблицы
sSL = sorted(l, key = lambda d: str(d['Gender']))
# Сортируем список при помощи лямбда-функции по столбцу с номером клиента из таблицы и переворачиваем список (reverse)
nSL = sorted(l, key = lambda d: str(d['N']), reverse = True)

print("Сортировка по строковому полю (полу):\n", sSL)
print("Сортировка по числовому полю (номеру посетителя) в обратном порядке (reverse):\n", nSL)

newL = []

"""

# Вывод информации по времени
newL = list(filter(lambda x: datetime.datetime.strptime(x['Time'], '%H:%M').hour > 12, l))
print(newL)

"""

# Отбор посетителей по онлайну (только те, кто в данный момент находится в магазине)
newL = list(filter(lambda x: x['Online'] == 'TRUE', l))
print("Пользователи, который в данный момент онлайн:\n", newL)

# Создаём файл для записи
with open("C:\\Users\\Admin\\PycharmProjects\\DPA\\lab3\\output.csv", 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = reader.fieldnames)  # Класс writer служит для записи данных в файл
    writer.writeheader()  # Записываем заголовок таблицы

    for row in sSL:
        # Метод writerow записывает параметр строки row в файл
        writer.writerow(row)

    for row in nSL:
        writer.writerow(row)

    for row in newL:
        writer.writerow(row)

print()
print("Пожалуйста, проверьте выходной файл")