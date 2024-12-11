import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.count = 100
        self.count_days = 0

    def fight(self):
        days = 1
        while self.count:
            self.count -= self.power
            print(f'{self.name} сражается {days} дней(дня), осталось {self.count} воинов.\n', end='')
            days += 1
            self.count_days += 1
            time.sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()
        print(f'{self.name} одержал победу спустя {self.count_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
second_knight.join()
first_knight.join()

print('Все битвы закончились!')


