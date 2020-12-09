from p5 import *
import serial

ser = None
r = 0
g = 0
b = 0


def setup():
    global ser
    ser = serial.Serial('/dev/ttyACM0')


def draw():
    global r, g, b
    background(r, g, b)
    fill(255 - r, 255 - g, 255 - b)
    text(f"fill({r},{g},{b})", 10, 50)
    if ser.in_waiting:
        line = ser.readline()
        r, g, b = [int(n) for n in line.strip().split(b',')]

run()
