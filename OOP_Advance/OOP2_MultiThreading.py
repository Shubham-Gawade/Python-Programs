# MultiThreading

from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()  #main thread will wait for completing t1 and t2
t2.join()
print("Bye")

#here are 3 threads created,1)Main thread -> "Bye" 2)t1 -> "Hello" 3)t3 -> "Hi"
