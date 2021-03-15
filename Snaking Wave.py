NUMLEDS = 66
counter = 0
counter2 = 0
tail = 10

RTail =220
GTail =0
BTail =100

RBack =50
GBack =135
BBack =168

import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, NUMLEDS)

pixels.fill((RBack,GBack,BBack))
while True:
    for counter in range (NUMLEDS):
        pixels[counter] = (RTail,GTail,BTail)
        time.sleep(0.01)
        pixels[counter-tail] = (RBack,GBack,BBack)
        time.sleep(0.01)
        print("counter")
        print(counter)
