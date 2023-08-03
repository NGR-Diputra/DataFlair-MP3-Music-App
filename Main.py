from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#Root Window
root = Tk()
root.title(" DataFlair Python MP3 Music Player App ")

#mixer
mixer.init()

def addsong():
    #return list of songs
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a Song", filetypes=(("mp3 files", "*.mp3"),))

    #loop the list
    for s in temp_song:
        

#listbox for the songs
song_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=("arial", 15), height=12, width=47, selectbackground="grey", selectforeground="black")
song_list.grid(columnspace=9)

#font defined, used for the button font
define_font = font.font(family="Helvetica")

#play button
play_button = Button(root, text="Play", width=7, command=Play)
play_button['font']=define_font
play_button.grid(row=1, column=0)

#Pause Button
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font']=define_font
pause_button.grid(row=1, column=1)

#stop Button
stop_button = Button(root, text="Stop", width=7, command=Stop)
stop_button['font']=define_font
stop_button.grid(row=1, column=2)

#resume Button
resume_button = Button(root, text="Resume", width=7, command=Resume)
resume_button['font']=define_font
resume_button.grid(row=1, column=3)

#previous Button
previous_button = Button(root, text="Previous", width=7, command=Previous)
previous_button['font']=define_font
previous_button.grid(row=1, column=4)

#next Button
next_button = Button(root, text="Next", width=7, command=Next)
next_button['font']=define_font
next_button.grid(row=1, column=5)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)


mainloop()