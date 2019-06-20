import controller
import camera
import threading

def co():
    controller()

def ca():
    camera()

threads = []
t1 = threading.Thread(target = co)
threads.append(t1)
t2 = threading.Thread(target - ca)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

