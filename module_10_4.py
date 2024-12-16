import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rand = random.randint(3, 10)
        time.sleep(rand)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for table in self.tables:
            if table.guest is None:
                table.guest = guests
                thread = threading.Thread(target=table.guest[table].run)
                thread.start()
                print(f'{Guest.name} сел(-а) за стол номер {self.tables}')
            else:
                self.queue.put(guests)
                print(f'{Guest.name} в очереди')

    def discuss_guests(self):
        for table in self.tables:
            if not table.guest is None and table.guest.is_alive():
                print(f'{table.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {self.tables} свободен')
                table.guest = None
            if not self.queue.empty() and table.guest is None:
                table.guest = self.queue.get
                print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables}')
                thread = threading.Thread(target=table.guest[table].run)
                thread.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()