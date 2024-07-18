import serial
import keyboard
import time
import sys

#PSerial 3.5 is in use for this example
#
#Press key 'x' to EXIT

CONST_SER_PORT = 'COM3'   #get the com port from device manger and enter it here

serDataq = serial.Serial(
    port = CONST_SER_PORT,
    timeout= 0.5
    )

serDataq.write(b"stop\r")        #stop in case device was left scanning
serDataq.write(b"encode 0\r")    #set up the device for binary mode
serDataq.write(b"slist 0 0\r")   #scan list position 0 channel 0 thru channel 7
serDataq.write(b"slist 1 1\r")   #scan list position 0 channel 0 thru channel 7
serDataq.write(b"slist 2 2\r")   #scan list position 0 channel 0 thru channel 7
serDataq.write(b"srate 6000\r")
serDataq.write(b"dec 100\r")
serDataq.write(b"deca 3\r")
serDataq.write(b"ps 0\r")        #if you modify sample rate, you need modify this accordingly
time.sleep(0.5)
while True:
    try:
        i= serDataq.in_waiting
        if i>0:
            response = serDataq.read(i)
            break
    except:
        pass
 
serDataq.reset_input_buffer()
serDataq.write(b"start\r")       #start scanning

numofchannel=3 #if you modify the slist, you need modify this accordingly
numofbyteperscan=2*numofchannel

while True:
    try:
        if keyboard.is_pressed('x'):    #if key 'x' is pressed, stop the scanning and terminate the program
            serDataq.write(b"stop\r")
            time.sleep(1)           
            serDataq.close()
            print("Good-Bye")
            break
        else:
            i= serDataq.in_waiting
            if (i//numofbyteperscan)>0:
                #we always read in scans
                response = serDataq.read(i - i%numofbyteperscan)

                Channel =[]

                for x in range (0, numofchannel):
                    adc=response[x*2]+response[x*2+1]*256
                    if adc>32767:
                        adc=adc-65536
                    Channel.append (adc)
    
                #Print only the first scan for demo purpose
                print ("%5d %5d %5d" %(Channel[0], Channel[1], Channel[2]))
            pass
    except:
        pass