class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year



class Printer(Equipment):

    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает с пк на листочек'

    def __str__(self):
        return f'{self.series}, {self.name}, {self.make}, {self.year}. Функции: {self.action()}'



class Scaner(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует на пк'



class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует и печатает на листочек'

def allItem(sklad):
    for item in sklad:
        print(item)

def get_items(skald, ename):
    for item in sklad:
        if isinstance(item, ename):
            print(item)


sklad = []
e = Equipment('Solaris', 'Hyndai', 2020)
sklad.append(e)
s = Printer('20A', 'Creta', 'Hyndai', 1990)
sklad.append(s)
x = Xerox('dsffs', 'asfsaf', 3252)
sklad.append(x)
e = Equipment('Solaris', 'Hyndai', 2020)
sklad.append(e)
s = Printer('20A', 'Creta', 'Hyndai', 1990)
sklad.append(s)
x = Xerox('dsffs', 'asfsaf', 3252)
sklad.append(x)
# allItem((sklad))
get_items(sklad, Equipment)
