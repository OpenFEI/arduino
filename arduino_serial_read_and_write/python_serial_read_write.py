#!/usr/bin/python
import serial
import syslog
import time

#defining Arduino port, baudrate, timeout
ard = serial.Serial( '/dev/ttyACM1', 9600, timeout=5)
time.sleep(3) #wait Arduino

i = 0

while (i < 4):
    # Serial write section
    setTempCar1 = 'FEI'
    setTempCar2 = 10
    ard.flush()
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print ("Python value sent: ")
    print (setTemp1)
    ard.write(setTemp1)
    time.sleep(1)
    print (setTemp2)
    ard.write(setTemp2)
    time.sleep(1)

    # Serial read section
    msg = ard.read(ard.inWaiting())
    print ("Message from arduino: ")
    print (msg)
    i = i + 1
else:
    print "Exiting"
exit()
