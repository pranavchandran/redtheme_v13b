# communicating with serial Ports
# serial port communicating 

import serial
ser = serial.Serial('/dec/tty.usbmode641', baudrate=9600,bytesize=8,parity='N',stopbits=1)
# print(ser)
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
