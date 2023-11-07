# class Point:
#     f = 0
#
#
#     def __new__(cls, *args, **kwargs):
#         print('method new')
#         return super(). __new__(cls)
#
#     def __init__(self, y, x=0):
#         self.x = x
#         self.y = y
#
#
# p = Point(2,8)
# print(p.x)
import ssl


# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def __del__(self):
#         print('Отключение соединения')
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')
#
#     def close(self):
#         print("Соединение разорвано")
#
#     def read(self):
#         print('Чтение данных')
#
#     def write(self, data):
#         print(f'Записываем данииые {data}')
#
#
# db = DataBase('user1', 'psw1', '`8000`')
# db2 = DataBase('user1', 'psw1', '`8000`')
# db.connect()
# print(db)
# print(db2)

class Test:
    # pass

    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return 'Тестирование объекта'

    def __str__(self):
        return f'Наименование {self.name}'


t = Test('pc')
t2 = Test('phone')
print(t)
print(t2)