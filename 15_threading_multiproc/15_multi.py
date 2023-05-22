#from multiprocessing import Process
from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

#processes = []
#num_processes = os.cpu_count()
threads = []
num_thread = 10

# # create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# create threads
for i in range(num_thread):
    t = Thread(target=square_numbers)
    threads.append(t)

# # start
# for p in processes:
#     p.start()

for t in threads:
    t.start()

# # join 
# for p in processes:
#     p.join()

for t in threads:
    t.join()

print('end main')
