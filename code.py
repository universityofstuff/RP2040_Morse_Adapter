import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Pins (GP14 = Blue/Dit, GP15 = Red/Dah)
dit = digitalio.DigitalInOut(board.GP14)
dit.direction = digitalio.Direction.INPUT
dit.pull = digitalio.Pull.UP

dah = digitalio.DigitalInOut(board.GP15)
dah.direction = digitalio.Direction.INPUT
dah.pull = digitalio.Pull.UP

# Track the live USB state to prevent spamming the computer
dit_state = False
dah_state = False

while True:
    # Read the physical pins (True if pressed)
    dit_pressed = not dit.value
    dah_pressed = not dah.value

    # Handle Dit Paddle
    if dit_pressed and not dit_state:
#        kbd.press(Keycode.LEFT_CONTROL)
        kbd.press(Keycode.LEFT_BRACKET)
        dit_state = True
    elif not dit_pressed and dit_state:
#        kbd.release(Keycode.LEFT_CONTROL)
        kbd.release(Keycode.LEFT_BRACKET)
        dit_state = False

    # Handle Dah Paddle
    if dah_pressed and not dah_state:
#        kbd.press(Keycode.RIGHT_CONTROL)
        kbd.press(Keycode.RIGHT_BRACKET)
        dah_state = True
    elif not dah_pressed and dah_state:
#        kbd.release(Keycode.RIGHT_CONTROL)
        kbd.release(Keycode.RIGHT_BRACKET)
        dah_state = False

    # Small 2ms delay purely to prevent contact bouncing
    time.sleep(0.002)
