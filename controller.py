import RPi.GPIO as GPIO
import time
import cv2
import requests
a = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15
ENA = 16
ENB = 18
GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(INT3,GPIO.OUT)
GPIO.setup(INT4,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)

pwma = GPIO.PWM(16,80)
pwmb = GPIO.PWM(18,80)
pwma.start(90)
pwmb.start(90)
url = 'http://120.78.174.107:8090/path'
response = requests.get(url)
maps = response.json()
GPIO.output(INT1, GPIO.LOW)
GPIO.output(INT2,GPIO.LOW)
GPIO.output(INT3,GPIO.LOW)
GPIO.output(INT4,GPIO.LOW)

pwma.ChangeDutyCycle(25)
pwmb.ChangeDutyCycle(15)
def runningcv():
    GPIO.output(INT3,GPIO.HIGH)
    GPIO.output(INT4,GPIO.LOW)
    time.sleep(20)
    GPIO.output(INT4,GPIO.HIGH)
    GPIO.output(INT3,GPIO.LOW)
    time.sleep(20)
    GPIO.output(INT3,GPIO.LOW)
    GPIO.output(INT4,GPIO.LOW)

def go():
    print('[INFO]GOING')
    GPIO.output(INT1,GPIO.HIGH)
    GPIO.output(INT2,GPIO.HIGH)

def right():
    print('[INFO]RIGHT')
    GPIO.output(INT1,GPIO.LOW)
    GPIO.output(INT2,GPIO.HIGH)

def left():
    print('[INFO]LEFT')
    GPIO.output(INT1,GPIO.HIGH)
    GPIO.output(INT2,GPIO.LOW)

def stop():
    GPIO.output(INT1,GPIO.LOW)
    GPIO.output(INT2,GPIO.LOW)
    
print('\033[1;30;41m[INFO]\033[0mCar is running')
def run(a,b):
    a = int(a)
    b = int(b)
    if a == 2:
        go()
        time.sleep(b)
    if a == -1:
        stop()
    if a == 4:
        runningcv()
    if a == 1:
        right()
        time.sleep(b)
    if a == 0:
        left()
        time.sleep(b)
def start():
    for maptip in maps:
        a = maptip['direction']
        b = maptip['len']
        run(a, b)
    print('[INFO]MOVE OVER')
    stop()


    print('[INFO]Program Over!')

