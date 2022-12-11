import os
import time
from threading import Thread
from multiprocessing import Process
doc_list = []
data_path_root = ('./data/')
data_path = os.listdir(data_path_root)

t1 = time.time()
for i in data_path:
    with open(os.path.join(data_path_root,i),'r') as file:
        doc_list.append(file.read())
t2 = time.time()
print(t2-t1)




t1 = time.time()
def read_file(filename):
    with open(os.path.join(data_path_root,i),'r') as file:
        file.read()
for i in range(len(data_path),6000):
    processes = []
    for data in data_path[i:i+6000]:
        p = Process(target=read_file,args=(data,))    
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
t2 = time.time()
print(t2-t1)


# t1 = time.time()
# processes = []
# for i in data_path:
#     p = Process(target=read_file,args=(i,))
#     processes.append(p)
#     p.start()

# for p in processes:
#     p.join()
# t2 = time.time()
# print(t2-t1)