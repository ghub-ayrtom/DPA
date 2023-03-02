# Родительский класс
class Music:
    # Конструктор класса
    def __init__(self, bpm, instruments, volume):
        self._bpm = bpm
        self._instruments = instruments
        self._volume = volume

    # "Сеттер"
    def setBPM(self, newBPM):
        if newBPM <= 240:
            self._bpm = newBPM

    # "Геттер"
    def getBPM(self):
        return self._bpm


# Дочерний класс
class HipHop(Music):  # Наследование
    def __init__(self, bpm, instruments, volume, home, legend, yearOfBirth):
        super().__init__(bpm, instruments, volume)  # super вызывает конструктор родительского класса
        self.__home = home
        self.__legend = legend
        self.__yearOfBirth = yearOfBirth

    def setLegend(self, newLegend):
        self.__legend = newLegend

    def getLegend(self):
        return self.__legend

    def singSomething(self):
        print("I'm representing for them gangstas all across the world\n"
              "(Still) Hitting them corners in them low-lows, girl\n"
              "Still taking my time to perfect the beat\n"
              "And I still got love for the streets, it's the D-R-E\n"
              '\n'
              "I'm representing for them gangstas all across the world\n"
              "(Still) Hitting them corners in them low-lows, girl\n"
              "Still taking my time to perfect the beat\n"
              "And I still got love for the streets, it's the D-R-E\n")


class Pop(Music):
    def __init__(self, bpm, instruments, volume, home, legend, yearOfBirth):
        super().__init__(bpm, instruments, volume)
        self.__home = home  # Инкапсуляция
        self.__legend = legend  #
        self.__yearOfBirth = yearOfBirth  #

    def setLegend(self, newLegend):  #
        self.__legend = newLegend  #

    def getLegend(self):  #
        return self.__legend  #

    def singSomething(self):
        print("I said, ooh, I'm blinded by the lights\n"
              "No, I can't sleep until I feel your touch\n"
              "I said, ooh, I'm drowning in the night\n"
              "Oh, when I'm like this, you're the one I trust\n"
              "(Hey, hey, hey)\n")


class Rock(Music):
    def __init__(self, bpm, instruments, volume, home, legend, yearOfBirth):
        super().__init__(bpm, instruments, volume)
        self.__home = home
        self.__legend = legend
        self.__yearOfBirth = yearOfBirth

    def setLegend(self, newLegend):
        self.__legend = newLegend

    def getLegend(self):
        return self.__legend

    # Полиморфизм
    def singSomething(self):
        print("Hello, hello, hello, how low?\n"
              "Hello, hello, hello, how low?\n"
              "Hello, hello, hello, how low?\n"
              "Hello, hello, hello\n")


# Создание экземпляров классов
g1 = HipHop(70, ["Drum machine", "Synthesizer", "Vinyl turntable"], "Medium", "USA", "Tupac Amaru Shakur (2Pac)", 1974)
g2 = Pop(125, ["Drums", "Guitar", "Synthesizer"], "Below average", "UK", "Taylor Alison Swift", 1950)
g3 = Rock(85, ["Bass Guitar", "Drums", "Solo Guitar"], "High", "USA", "The Beatles (band)", 1954)

print(g1.getBPM())  # get - получить значение свойства
g1.setBPM(95)
print(g1.getBPM())
print()

g2.setLegend("Michael Joseph Jackson")  # set - присвоить значение свойству

# Образно получаем из базы данных список музыкальных жанров, популярные песни которых мы хотим услышать на образном концерте
musicGenres = [g1, g2, g3]

# Полиморфизм
for popularSong in musicGenres:
    popularSong.singSomething()  # Весело поём на образном концерте популярные песни каких-то музыкальных жанров
