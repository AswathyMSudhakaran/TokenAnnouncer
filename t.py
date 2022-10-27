#Import the required Libraries
from tkinter import *
from tkinter import ttk
from ast import GtE
from gtts import gTTS
from playsound import playsound
import os
win = Tk()
win.geometry("750x250")
def get_content():
    txt="ടോക്കൺ നമ്പർ"+entry.get()
    tts = gTTS(txt, lang = 'ml')
    file1 = str("hello" + str(1) + ".mp3")
    tts.save(file1)
    playsound(file1)
    os.remove(file1)
    entry.delete(0,END)
labe=Label(win,text="Its Aswathys Token announcer",width=40)
labe.pack(pady=20)
entry= Entry(win, width= 40)
entry.pack(pady= 20)
button= ttk.Button(win, text= "Call Token", command= get_content)
button.pack(pady=10)
win.mainloop()