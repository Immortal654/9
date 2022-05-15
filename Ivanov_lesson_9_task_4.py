class Car:
    is_police = False

    def __init__(self, color, name):
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f"Машина модели {self.name} тронулась, скорость {self.speed}.")

    def stop(self):
        self.speed = 0
        print(f"Машина модели {self.name} остановилась.")

    def turn(self, direction):
        if direction == "лево" or direction == "право":
            print(f"Машина модели {self.name} повернула на {direction}.")
        else:
            print(f"Машина запрограммирована поворачивать на лево и на право.")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(f"Ваша скорость равна {self.speed}, что превышает допустимую скорость.")
        else:
            print(f"Скорость автомобиля {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(f"Ваша скорость равна {self.speed}, что превышает допустимую скорость.")


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar("синий", "Шкода")
auto_1.go(20)
auto_2 = SportCar("чёрный", "Ламба")
auto_2.go(80)
auto_2.show_speed()
auto_2.turn("право")
auto_3 = WorkCar("белый", "Мерс")
auto_3.go(43)
auto_3.show_speed()
auto_4 = TownCar("красный", "Ауди")
auto_4.go(65)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
