# from threading import Thread, Lock
# import time 

# database_value = 0

# def increase(lock):
#     global database_value

#     with lock:
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy

# if __name__ == "__main__":

#     lock  = Lock()
#     print('start value', database_value)

#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('end value', database_value)
 
#     print('end main')

# start value 0
# end value 1
# end main

# start value 0
# end value 2
# end main





# ===== Use queues ======
# Queue - linear data structure that follows the FIFO  
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()
        # processig ...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()
        # if ...:
        #     break

if __name__ == "__main__":
     
    q = Queue()
    lock = Lock()
    num_threads = 10 

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon=True # if don't use - programm will still continue here in our wild true loop
        # thread.daemon=False
        thread.start()

    for i in range(1, 21):
        q.put(i)
    
    q.join()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3 2 1 --> 
    # first = q.get()
    # print(first)

    # q.task_done()
    # q.join()
    

    print('end main')


# in Thread-1 (worker) got 1
# in Thread-2 (worker) got 2
# in Thread-5 (worker) got 4
# in Thread-6 (worker) got 6
# in Thread-8 (worker) got 8
# in Thread-10 (worker) got 10
# in Thread-3 (worker) got 3
# in Thread-4 (worker) got 5
# in Thread-5 (worker) got 13
# in Thread-6 (worker) got 14
# in Thread-8 (worker) got 15
# in Thread-10 (worker) got 16
# in Thread-2 (worker) got 12
# in Thread-7 (worker) got 7
# in Thread-9 (worker) got 9
# in Thread-1 (worker) got 11
# in Thread-4 (worker) got 18
# in Thread-3 (worker) got 17
# in Thread-6 (worker) got 20
# in Thread-5 (worker) got 19
# end main

