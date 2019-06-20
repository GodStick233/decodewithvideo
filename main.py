import controller
import camera
import threading
import time
def co():
    print(time.ctime())
    controller.start()

def ca():
    print(time.ctime())
    camera.start()

threads = []
t1 = threading.Thread(target = ca)
threads.append(t1)
t2 = threading.Thread(target = co)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

