# SoundboardProject

This is a soundboard project that I coded in python. The intent I had with this code is to play sounds over my microphone on applications such as discord so that I can talk and play sounds at the same time. To do this I use external software. The link to the software I used as well as some basic instructions about how to set them up will be linked in a section below.  

Using External Software

The external software I used are https://vb-audio.com/Cable/, for a virtual audio cable, and https://vb-audio.com/Voicemeeter/index.htm, to join the audio inputs into one. These are not the only options for this purpose, but these are both free.  For the virtual audio cable, the deviceName variable should be used to direct the output to a virtual audio cable. You can listen to the this at the same time by opening up the sound settings and turn on listen to this device. Then set the output device to the default device you use. The next step is to join your input devices (microphone and virtual audio cable). This is where the voicemeeter software is used. You set the first input device to be your speaker and then you set the second input device to be the output cable. Then the cable with both audio and soundboard should be output cable b1.

Using Python Only

The Python only file is soundboard.py. This soundboard triggers whenever a number key is pressed detecting whenever a key is pressed. This currently limits the number of sounds able to be played to 10 (0-9). This could be changed tweaking the way that the key inputs are detected. The other thing that is that only mp3 files are detected with this code, but pygame mixer does allow for more files to be played than just mp3 files. Without using external software the only thing that needs to be changed is that the variable deviceName isn’t used and mixer.init(devicename=deviceName) should be changed to mixer.init().

Using Python and Arduino

The files needed for this is numpad.ino and soundboardarduino.py. Communication between the Python and Arduino is done using serial communication. In this case it is done over the COM3 port. To run this code, first run the Arduino code and then the Python code. One thing to note is that having the COM3 port tab open on the Arduino will make it so that the Python program will not connext. This is due to the fact that a port only has two usable sides. The Arduino I used for this was an Arduino mega. The hardware I used was a 4x4 membrane keypad for input. The soundboard will trigger whenever a key is pressed. Without using external software the only thing that needs to be changed is that the variable deviceName isn’t used and mixer.init(devicename=deviceName) should be changed to mixer.init(). Those are both in the python file.


