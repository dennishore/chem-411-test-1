from display import max7219
import time

display = max7219.SevenSegment(digits=16, scan_digits=8, cs=5, spi_bus=2, reverse=True)

while True:
    display.text("ABCDEF")
    time.sleep(1)
    display.number(3.14159)
    time.sleep(1)
    display.message("Hello World")
    time.sleep(1)
    display.clear()