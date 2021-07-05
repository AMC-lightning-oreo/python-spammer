
from pynput.keyboard import Key, Controller
import time
#the above shows how to pull the necessary packages for this to work! If you do not already have the package, you can download it with the "pip install pynput" command!


message = "Hi I am the message to be spammed! Join our server discord.gg/help today!"
#obviously, you can change the message above to something else!

keyboard = Controller()
#this pulls for the keyboard's functions within the previously mentioned packages!
time.sleep(.1)
#suspends execution for the given number of seconds
 
#line 16 is the repetitive system, however, it is adjusted to a certain number of times for the messages to work!
#lines 18 to 20 shows the content within the message being replicated, letter by letter! However, it is reported to have crashed while trying to send out zalgo characters! (I have not seen it myself yet)
for num in range(10000):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(.1)
#lines 21 and 22 types the "enter" key! It is like a keyboard, but a virtual one! It replicates the system(possibly signal/electrical impulses) of a keyboard without actually needing a keyboard!
#line 23 suspends execution for the given number of seconds before a repeat
