from random import random
from time import sleep
from pygame import mixer
import os
import serial

#making a serial object to use serial communication
arduino = serial.Serial('COM3', 9600, timeout=1)

''' This code is for a soundboard that triggers whenever a number key is pressed
This is done using read_key so the person isn't prompted for the key
Sounds will play over each other, they will not wait for others to finish
Due to current designs, number of sounds in the soundboard cannot exceed 10
If this limit is exceeded then sounds assigned numbers 10 and up cannot be played
To add more than 10 sounds, use a switch statement to control indexes into mp3_files'''

EXITKEY = 'A' #key pressed to break the loop
STOPKEY = 'B' #key pressed to stop all current played sounds
PAUSEKEY = 'D'
filePath = "C:/Users/vikra/PycharmMiscProject/sounds" #where the sound files are located
deviceName = 'CABLE Input (VB-Audio Virtual Cable)' #where you want the audio to go

TIMEDELAY = 0.2 #the time delay between keys being read

if __name__ == '__main__':

    mp3_files = [file for file in os.listdir(filePath) if file.endswith('.mp3')]
    #mp3_files is a list containing all of the mp3 files in the filepath
    #this can be changed to include other file types

    #printing all of the mp3 files in mp3_files
    temp = 0
    print("Sound file and number to play the file")
    for file in mp3_files:
        print(file, ": ", temp)
        temp += 1

    print("enter " + EXITKEY + " to exit")
    print("enter " + STOPKEY + " to stop all sounds")
    print("enter " + PAUSEKEY + " to pause the soundboard")

    mixer.init(devicename=deviceName) #initializing the mixer
    sounds = [] #list of active sounds
    paused = False

    while True: #this loop waits for the arduino and python scripts to be connected then breaks
        response = arduino.readline().decode('utf-8').strip()
        if response == "starting": #if you change this here, make sure to change it in the arduino file
            print("connected")
            break

    while True:
        response = arduino.readline().decode('utf-8').strip()
        response = str(response)

        if response == EXITKEY: #exiting the loop
            break

        if response == PAUSEKEY:
            sleep(TIMEDELAY)
            for temp in sounds:
                    temp.stop()
            sounds = []  # clearing the array
            if paused: #flipping paused
                paused = False
            else:
                paused = True

        if paused == False:
            if response == STOPKEY: #stopping all sounds
                for temp in sounds:
                    temp.stop()
                sounds = [] #clearing the array
            elif response.isdigit(): #only checking for number keys
                sound_index = int(response)
                if sound_index < len(mp3_files): #checking bounds on the input
                    sound = mp3_files[sound_index] #finding the given sound in mp3_files
                    full_path = os.path.join(filePath, sound) #getting the filepath of the sound
                    tempsound = mixer.Sound(full_path)
                    sounds.append(tempsound) #adding tempsound to the array of sounds
                    tempsound.play()
                    print("Playing:", sound)
                    sleep(TIMEDELAY) #to not play the same sound multiple times
