import max7219
display = max7219.SevenSegment(digits=16, scan_digits=8, cs=5, spi_bus=1, reverse=True)
display.text("ABCDEF")
display.number(3.14159)
display.message("Hello World")
display.clear()