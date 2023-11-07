import random

class Soldier:

    def __init__(self, name='Noname', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        rand = random.randint(1, 20)
        enemy.health -= rand
        print('Удар на', rand ,'здоровья')
        if enemy.health < 0:
            enemy.health = 0

        self.health += rand // 2
        print('Пополнение здоровья на', rand // 2)
        print(self.name, 'бьет', enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))


class Battle:

    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = 'Сражение не было'

    def battle(self):
        while self.u1.health > 0 and self.u2.health > 0:
            n = random.randint(1, 2)
            if n == 1:
                self.u1.make_kick(self.u2)
            else:
                self.u2.make_kick(self.u1)

        if self.u1.health > self.u2.health:
            self.result = self.u1.name + ' Победил'

        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + ' Победил'

    def who_win(self):
        print(self.result)





first = Soldier('Mr. First1',140)
second = Soldier()
second.set_name('Mr. Second2')
b = Battle(first,second)
b.battle()
b.who_win()