import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    leds[0].value = 0
    leds[1].value = 0
    leds[2].value = 0
    leds[3].value = 0
    leds[4].value = 0
    leds[5].value = 0
    leds[6].value = 0
    leds[7].value = 0
    leds[8].value = 0
    leds[9].value = 0
    leds[10].value = 0

    if (volume > 1000):
        leds[0].value = not leds[0].value
    if (volume > 2000):
        leds[1].value = not leds[1].value
    if (volume > 3000):
        leds[2].value = not leds[2].value
    if (volume > 4000):
        leds[3].value = not leds[3].value
    if (volume > 4500):
        leds[4].value = not leds[4].value
    if (volume > 5000):
        leds[5].value = not leds[5].value
    if (volume > 5500):
        leds[6].value = not leds[6].value
    if (volume > 6000):
        leds[7].value = not leds[7].value
    if (volume > 6500):
        leds[8].value = not leds[8].value
    if (volume > 7000):
        leds[9].value = not leds[9].value
    if (volume > 7500):
        leds[10].value = not leds[10].value

    sleep(0.05)


    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?