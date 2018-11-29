# tm1637-pi-python
A modification to Tim Waizenegger's tm1637.py library for simple TM1637 operation via raspberry pi. Full credit to Waizenegger for a majority of the library. View the original material here: https://github.com/timwaizenegger/raspberrypi-examples/blob/master/actor-led-7segment-4numbers/tm1637.py
This version of the library simply includes a new ShowScroll function which allows the user to display an integer of any length on the TM1637.

## Getting Started

The following instructions will get the example provided in tm1637_exploration.py to run using the library.

### Setup

Start by simply downloading/copying the library and the test file into the same directory on your Pi. 
Once done, be sure to check line 6 in the test file:
```
display = tm1637_alt.TM1637(CLK=23, DIO=24, brightness=2.0)
```
Set the value of CLK and DIO to whichever Pi GPIO pins you have used. If you copy the hardware setup below, this will work as is.

### Running

Navigate into the directory where you have stored the files you just downloaded. You can then run the program with Python3. For those unfamiliar with Linux, the following command will do the trick: 
```
sudo python3 tm1637_exploration.py
```

### Hardware Setup

Pretty straight-forward here. You can use any GPIO pins for CLK and DIO so long as you set them up correctly as shown above. No need for external power supply, the Pi 5V and ground works just fine.

PI | TM1637 Display
--- | --- 
GPIO 23 | CLK
GPIO 24 | DIO
5V | 5V
GND | GND

## Video

If you are interested in a quick showcase of what you can expect to see if you setup the hardware and software correctly, check out this video. 

Additionally, it quickly covers how to display any custom values you may want. This is covered quickly below as well. If you are going to expand upon the library here, I recommend this section of the video to pick up a basic understanding of the device's operation. Timestamp:


## Custom Display Values

If you are interested in displaying values that are not within the library, this section gives a brief rundown of how to do so.

### Understanding the Values

You may have noticed the HexDigits array near the top of the library. This array contains hex values for each hex value in order. If you would like to change this array or create your own function for displaying custom values, you'll want to know how to determine the hex value for your desired display. 
Fortunately it is pretty simple. The diagram below depicts which binary digits apply to which segment. 
![Image did not load.](https://github.com/Michael-Kirkpatrick/tm1637-pi-python/blob/master/readme-assets/CP320_TM1637.png)

### Example

Lets say you would like to depict an "L" on the display. Then you would want to light up segments DEF, which corresponds to the binary byte **00111000**. In hex, that would be **0x38**. Thus using **0x38** as your hex value that is written to the TM1637 will result in an L appearing.
![Image did not load.](https://github.com/Michael-Kirkpatrick/tm1637-pi-python/blob/master/readme-assets/CP320_TM1637_ExampleL.png)

### Understanding the Communication

Now that you have the hex value you want, you need to know how to actually write it to the device. There are multiple examples within the library for specifics (notably the Show function), but here is a quick rundown to make it easy.

*Note: This rundown uses the writeByte, start, stop, and br (terse break) functions already included in the library to make it simple. If for any reason you would like to know the exact values being passed at any time, you can do so by reading the functions in the library, or by checking the TM1637 datasheet for more information.*

1. Start the data transfer. We are going to write in auto increment mode.
2. Write the first command to signal for writing data to display register (0x40), then break. Write the second command which gives the first address to write to, it will auto increment for each value after this, so we will want to use the address of the first digit, which is 0xC0.
3. Send the data bytes for each display sequentially. This is where you send the byte you want to write to the writeByte function. Do this for each display digit. If you wanted the L in the first 7 segment display and nothing else, you would write 0x38, and then write 0x00 for the other 3 displays.
4. Break, and then write the third command, which controls the display's pulse width. We want the display ON, so our base value is 0x88. We can then add a value between 0-7 to that to control the brightness of the display. For example, if we want a brightness of 2, we add 2 to 0x88 and get 0x8A. Write this value as the third command.
5. Lastly, we stop the data transfer, finishing our display.

**If you are still confused about the display, I suggest watching the video for a verbal explanation of the above.**
