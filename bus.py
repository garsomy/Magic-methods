class Bus:

    def __init__(self, capacity, max_speed):
        self.speed = 0
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.has_empty_seats = True
        self.seats = {}

        for i in range(1, capacity + 1):
            self.seats[i] = None

    def embark_passenger(self, passenger_name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            for seat, name in self.seats.items():
                if name is None:
                    self.seats[seat] = passenger_name
                    break
            self.update_has_empty_seats()
        else:
            print("Автобус полный.")

    def disembark_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            for seat, name in self.seats.items():
                if name == passenger_name:
                    self.seats[seat] = None
                    break
            self.update_has_empty_seats()
        else:
            print(f"Пассажир {passenger_name} не в автобусе.")

    def increase_speed(self, value):
        if self.speed + value > self.max_speed:
            print("Скорость максимальна.")
        else:
            self.speed += value

    def decrease_speed(self, value):
        if self.speed - value < 0:
            print("Скорость не может быть отрицательной.")
        else:
            self.speed -= value

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.embark_passenger(passenger_name)
        return self

    def __isub__(self, passenger_name):
        self.disembark_passenger(passenger_name)
        return self

    def update_has_empty_seats(self):
        self.has_empty_seats = len(self.passengers) < self.capacity


bus = Bus(5, 60)
print("Начало:")
print("Скорость:", bus.speed)
print("Места:", bus.capacity)
print("Максимальная Скорость:", bus.max_speed)
print("Пассажиры:", bus.passengers)
print("Свободные места есть?", bus.has_empty_seats)
print("Каккие и кем заняты места:", bus.seats)

print()

bus.embark_passenger("Глеб")
bus.embark_passenger("Кирилл")
bus.embark_passenger("Артём")
bus.increase_speed(50)

print("После посадки и ускорения:")
print("Скорость:", bus.speed)
print("Пассажиры:", bus.passengers)
print("Свободные места есть?", bus.has_empty_seats)
print("Каккие и кем заняты места:", bus.seats)

print()

bus -= "Алёна"
bus.decrease_speed(30)

print("После высадки и замедления:")
print("Скорость:", bus.speed)
print("Пассажиры:", bus.passengers)
print("Свободные места есть?", bus.has_empty_seats)
print("Каккие и кем заняты места:", bus.seats)

print()

if "Саша" in bus:
    print("Майк не в автобусе.")

bus += "Глеб"

print()

print("Итого:")
print("Скорость:", bus.speed)
print("Пассажиры:", bus.passengers)
print("Свободные места есть?", bus.has_empty_seats)
print("Каккие и кем заняты места:", bus.seats)
