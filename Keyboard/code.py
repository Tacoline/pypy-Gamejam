from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

last_tone = 0

def play(tone):
    global last_tone
    if last_tone != tone or last_tone == 0:
        cpx.stop_tone()
        cpx.start_tone(tone)
        last_tone = tone

def stop_playing():
    global last_tone
    cpx.stop_tone()
    last_tone = 0

def resetLed():
    for i in range(10):
        cpx.pixels[i] = (0, 0, 0)

def setLed(num, color):
    for i in range(10):
        if i == num:
            cpx.pixels[i] = color
        else:
            cpx.pixels[i] = (0, 0, 0)

while True:
    if cpx.touch_A1:
        setLed(6, 0xFF0000)
        play(262)
    elif cpx.touch_A2:
        setLed(7, 0xFF8C00)
        play(294)
    elif cpx.touch_A3:
        setLed(8, 0xFFFF00)
        play(330)
    elif cpx.touch_A4:
        setLed(0, 0x008000)
        play(349)
    elif cpx.touch_A5:
        setLed(1, 0x0000FF)
        play(392)
    elif cpx.touch_A6:
        setLed(3, 0x4B0082)
        play(440)
    elif cpx.touch_A7:
        setLed(4, 0xEE82EE)
        play(494)
    else:
        resetLed()
        stop_playing()
