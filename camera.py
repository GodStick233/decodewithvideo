import cv2
from pyzbar import pyzbar
import requests
import time
found = set()
capture = cv2.VideoCapture(0)
def start():
    print('[INFO]Camera is working')
    while(1):
        ret,frame = capture.read()
        test = pyzbar.decode(frame)
        for tests in test:
            testdate = tests.data.decode('utf-8')

            if testdate not in found:
                print('[INFO]Get code:' + testdate)
                url = 'http://120.78.174.107:8090/add?data=' + testdate
                requests.post(url)
                found.add(testdate)
        #cv2.imshow('Test',frame)
        if cv2.waitKey(1) == ord('q'):
                break
        
        
