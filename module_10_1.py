import time
import threading
import datetime

def write_words(word_count, file_name):
    number = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for line in range(word_count):
            time.sleep(0.1)
            file.write(f'Какое-то слово № {number}\n')
            number += 1
    print(f'Завершилась запись в файл {file_name}')

start_function = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_function = datetime.datetime.now()
result_work_function = finish_function - start_function
print(result_work_function)

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

start_flow = datetime.datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

finish_flow = datetime.datetime.now()
result_work_flow = finish_flow - start_flow
print(result_work_flow)