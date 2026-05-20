# two ways to create threads in python using classes using functions

from threading import Thread
from time import sleep

class Hello(Thread):

    def run(self):
        for i in range(5):
            print(f"Hello {i}")
            sleep(0.3)

class Hi(Thread):
    
    def run(self):
        for i in range(5):
            print(f"Hi {i}")
            sleep(0.3)

# t1 = Thread(target=Hello().run)  -- function based thread creation
# t2 = Thread(target=Hi().run)

if __name__ == "__main__":
    t1 = Hello()
    t2 = Hi()

    t1.start()
    t2.start()