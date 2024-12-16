import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

start_linearly = datetime.datetime.now()
read_info('file 1.txt')
finish_linearly = datetime.datetime.now()
result_linearly = finish_linearly - start_linearly
print(result_linearly)


# if __name__ == '__main__' :
#
#     list_ = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

#     start_multiproc = datetime.datetime.now()
#     with Pool(4) as p:
#         p.map(read_info, list_)
#     finish_multiproc = datetime.datetime.now()

#     result_multiproc = finish_multiproc - start_multiproc
#     print(result_multiproc)