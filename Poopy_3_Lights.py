import time
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_GREEN = LED(20)
button_GREEN = 25

led_RED = LED(21)
button_RED = 24

led_YELLOW = LED(16)
button_YELLOW = 23

button_QUIT = 18
play = True

GPIO.setup(button_GREEN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_RED, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_YELLOW, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_QUIT, GPIO.IN, GPIO.PUD_UP)

print("Please press buttons!")
print("Press white button to quit.")

while play:
    button_state_GREEN = GPIO.input(button_GREEN)
    button_state_RED = GPIO.input(button_RED)
    button_state_YELLOW = GPIO.input(button_YELLOW)
    button_state_QUIT = GPIO.input(button_QUIT)

    if button_state_GREEN == GPIO.LOW:
        print("GREEN")
        led_GREEN.on()
        time.sleep(0.5)
        led_GREEN.off()

    if button_state_RED == GPIO.LOW:
        print("RED")
        led_RED.on()
        time.sleep(0.5)
        led_RED.off()

    if button_state_YELLOW == GPIO.LOW:
        print("YELLOW")
        led_YELLOW.on()
        time.sleep(0.5)
        led_YELLOW.off()


    if button_state_QUIT == GPIO.LOW:
        print("--> Quit")
        play = False
    
    time.sleep(0.1)
