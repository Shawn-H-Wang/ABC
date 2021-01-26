# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/19 16:19
# @Filename: test.py
# @Software: PyCharm

"""
python Thread test
"""

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Thread Starting...")
        # Lock for the synchronization
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Unlock to start the next thread
        threadLock.release()


# Test for print current time
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()

if __name__ == '__main__':
    print("All starting...")

    # Threads list
    threads = []

    # Create two new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start the threads
    thread1.start()
    thread2.start()

    # Add threads to the thread list
    threads.append(thread1)
    threads.append(thread2)

    # Wait for all threads finished
    for t in threads:
        t.join()
    print("All finished")
