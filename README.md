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
Set the value of CLK and DIO to whichever Pi GPIO pins you have used. If you watched the video linked below and wired the TM1637 to the Pi the same way, this will work as is.

### Running

Navigate into the directory where you have stored the files you just downloaded. You can then run the program with Python3. For those unfamiliar with Linux, the following command will do the trick: 
```
sudo python3 tm1637_exploration.py
```

## Video Explanation

If you are interested in a basic tutorial of how the TM1637 operates, as well as how to go about creating your own custom functionality with the device, take a look at the video below.
The video also includes visuals of how I setup the Pi and TM1637 to run the test program if you are interested.
