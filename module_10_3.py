import threading
import random
import time


class Bank(threading.Thread):
    random_ = random.randint(50, 500)
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            self.balance += self.random_
            print(f'Пополнение: {self.random_} Баланс: {self.balance}')
            if self.balance >= 500 and self.lock == self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            print(f'Запрос на {self.random_}')
            if self.random_<= self.balance:
                self.balance -= self.random_
                print(f'Снятие: {self.random_}. Баланс: {self.balance}')
            if self.random_ > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


