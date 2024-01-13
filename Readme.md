# SSD1306 library with font size addition
I have multiple SSD1306 OLED screens, connected to Raspberry Pi Pico / micropython through an I2C multiplexer ```TCA9548A```, there are a lot 
of libraries on the net that have a font size change , but they either for arduino or the font is only enlarged which looks 
really not nice. I found one library on GitHub 
```html
https://github.com/jdhxyy/ssd1306py-micropython
```
BTW Hi kudos for the auther, but when I needed to update the values on the screen it took a lot of time updating on the screen,
which was almost 3 seconds to update 3 screens, so with the notes of ```https://github.com/ch686``` I have worked out this library.
## installation
Currently, the installation is only manual, I will be working one the setup later.

This library is based on Adafruit SSD1306 library:
```html
https://github.com/adafruit/micropython-adafruit-ssd1306.git
```
### First 
make sure that ```mpremote``` is installed 
```commandline
pip install mpremote
```
### Second 
Download the library as a zip file and extract it in you local drive
copy the lib directory and recursive folder and file with in it to your raspberry PI Pico, using the following command.
```commandline
mpremote cp -r lib/ :
```

To save space on pico you can always delete Unused font sizes.

All other functions of adafruit is still working.
the only difference is that I don't have a color of text option.


#### PS: If the raspberry pi is connected through Thonny disconnect it first.

## Using Library

Import the library 
```python
import ssd1306mp.ssd1306font as LCD
```
Initialize the lcd:
```Python
i2c = machine.I2C(0, sda=Pin(16), scl=Pin(17))
lcd = LCD.ssd1306font(width= 128, height = 64, i2c = i2c)
```
Send text :
```python
lcd.text_fb(String, x, y, font_size)
# x,y top left position of the string
# font size (8, 16, 24, 32, 48, 64) all sizes are included in the library 
```
you can check the test file.
```commandline
test_ssd1306mp.py
```

## Using other fonts
I used free font which comes with PCtoLCD2002, but if you have any preferred font you can easily add your font to this library.
you can download it from this repository:

```html
https://github.com/fishjump/PCtoLCD2002_exe.git
```
you must edit options to be similar to this image:

![PCtoLCD2002 options](images/PCtoLCD2002%20Options.png)

```
Mode must be Column by Column
Custom must be (A51??) Custom checkbox is selected
    Prefix = !!
    Suffix = Empty
    Comment Prefix = "
    Commect Suffix = ",
    Data Prefix = 0x
    Data Suffic = ,
    Line Prefix = Empty
    Line Suffix = ,
    Line Tail = !!
Data per line ( doesn't mater)
```
Select Mode to be as character Mode (W):

![PXtoLCD2002 Mode](images/PCtoLCD2002%20Mode%20selection.png)

Paste the following list for all printable letters 

```text
 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```
Paste in this field:

![PCtoLCD2002](images/PCtoLCD2002%20Letters%20field.png)

Select the font and Height:

![PCtoLCD2002](images/PCtoLCD2002%20Font%20and%20width.png)

Make sure that you can select a font height that can be divided by 8 
otherwise the tool will not work.
you can play with pixel position and padding to get the letters fit in middle.


generate and save the text file in this format ```Ascii{font size}.txt```
use the function ```Convert_TXT2BIN(font_size)``` in ```Tools.py``` to convert text file to bin format, save the font in ```lib\ssd1306font```
overwrite old files if needed.

upload the library again or add it by ```upload to``` command in thonny. 