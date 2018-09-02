# main.py
import pyb   # importing the board

switch = pyb.Switch()   # assigning the switch USR
accel = pyb.Accel()     # assigning the sensor to act as movement detector…
hid = pyb.USB_HID()     # assigning the HID (the USB mouse)

while not switch():     # while loop, looping while switch is not pressed…
    hid.send((0, accel.x(), accel.y(), 0))  # map moment on monitor based on the                                       movement of the board
    pyb.delay(20)                       # Delay by 20 microseconds to allow                                       visible movement (Not too fast!)
