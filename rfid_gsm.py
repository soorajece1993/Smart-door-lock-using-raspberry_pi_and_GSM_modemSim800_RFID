import serial
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(11,GPIO.OUT)

relayPin= 11

ser1 = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0.5)
ser2 = serial.Serial(port='/dev/ttyUSB1',baudrate=9600,timeout=0.5)

while True: # Run forever
    
    serdata=ser2.readline()
    ser2_data=serdata.decode('UTF-8')
    ser2_data = ser2_data.strip()
    if ser2_data == "0013957760":
        print("Access granted")
        GPIO.output(11,GPIO.HIGH)
        sleep(1)
        GPIO.output(11,GPIO.LOW)
        sleep(1)
        
        ser1.write(('AT+CMGF=1\r').encode())
        sleep(1)
        
        ser1.write(('AT+CMGS="+91XXXXXXXXXX"\r').encode())
        sleep(1)
        msg=("VRINDA")
        
        ser1.write((msg+chr(26)).encode())
        sleep(1)
        
    else if ser2_data == "0013950454":
        print("Access granted")
        GPIO.output(11,GPIO.HIGH)
        sleep(1)
        GPIO.output(11,GPIO.LOW)
        sleep(1)
        ser1.write(('AT+CMGF=1\r').encode())
        sleep(1)
        
        ser1.write(('AT+CMGS="+91XXXXXXXXXX"\r').encode())
        sleep(1)
        msg=("TINKU")
        
        ser1.write((msg+chr(26)).encode())
        sleep(1)
    
    else:
        print("Invalid Card")
        GPIO.output(11,GPIO.LOW)
        sleep(1)
        GPIO.output(11,GPIO.LOW)
        sleep(1)
        ser1.write(('AT+CMGF=1\r').encode())
        sleep(1)
        
        ser1.write(('AT+CMGS="+91XXXXXXXXXX"\r').encode())
        sleep(1)
        msg=("Invalid Card")
        
        ser1.write((msg+chr(26)).encode())
        sleep(1)
    








       
