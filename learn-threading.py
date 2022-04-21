import os
import threading
from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print('done')


start_time = perf_counter()

# create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')


def print_cube(num):
    """ function to print cube of given num """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """ function to print square of given num """
    print("Square: {}".format(num * num))


t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
t2.start()

# wait until thread 1 is completely executed
t1.join()
t2.join()

# both threads completely executed
print("Done!")

# Python program to illustrate the concept
# of threading


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


# print ID of current process
print("ID of process running main program: {}".format(os.getpid()))

# print name of main thread
print("Main thread name: {}".format(threading.current_thread().name))

# creating threads
t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

# starting threads
t1.start()
t2.start()

# wait until all threads finish
t1.join()
t2.join()


data = threading.Lock()
print("before first acquire")
data.acquire()
print("before second acquire")
data.release()
data.acquire()
print("acquired lock twice")
