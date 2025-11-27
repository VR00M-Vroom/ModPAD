# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.D, KC.W, KC.S, KC.A, KC.PSCR, KC.LWIN, KC.DELETE,   ]
]
oled_width = 128
oled_height = 32


oled = SSD1306(
    i2c=board.I2C(),       
    width=oled_width,
    height=oled_height,
    addr=0x3C,           
)


display = Display(oled)
keyboard.extensions.append(display)



@display.on_render
def render(oled):
    oled.fill(0)  # clear screen
    oled.text("KMK Firmware", 0, 0)
    oled.text("0.91\" OLED OK", 0, 10)
    oled.text("Layer: {}".format(keyboard.active_layers[0]), 0, 20)
    oled.show()

# Start kmk!
if __name__ == '__main__':
    keyboard.go()