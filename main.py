# import packages
import tkinter as tk
import fnmatch
import os
from pygame import mixer

# initiating the canvas properties
canvas = tk.Tk()
canvas.title("Classic Treasures")
canvas.geometry("400x600")
canvas.config(bg="black")
root_path = "assets\\sample music"  # giving file path
pattern = "*.mp3"  # extract only the extension with .mp3 format

mixer.init()  # initiating mixer

# button images
bk_img = tk.PhotoImage(file="assets/images/1.png")
prev_img = tk.PhotoImage(file="assets/images/buttons/prev_img.png")
stop_img = tk.PhotoImage(file="assets/images/buttons/stop_img.png")
play_img = tk.PhotoImage(file="assets/images/buttons/play_img.png")
pause_img = tk.PhotoImage(file="assets/images/buttons/pause_img.png")
next_img = tk.PhotoImage(file="assets/images/buttons/next_img.png")


# play button function
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(root_path + "\\" + listBox.get("anchor"))
    mixer.music.play()


# play button function
def stop():
    mixer.music.stop()
    listBox.select_clear("active")


# play button function
def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)

    mixer.music.load(root_path + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


# play button function
def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)

    mixer.music.load(root_path + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


# play button function
def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


# fonts initiation
f1 = ("playfair_display", 10)
f2 = ("waterfall", 25)

# button properties
bkButton = tk.Button(canvas, text="Music Player", image=bk_img, bg="black", borderwidth=0, command=stop)
bkButton.pack(pady=15)

# song list
listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=f1)
listBox.pack(padx=40, pady=15)

label = tk.Label(canvas, text='', bg="black", fg="white", font=f2)
label.pack(pady=15)

# button frame
top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

# buttons
prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg="black", borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="black", borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg="black", borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg="black", borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg="black", borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

# read each file in the root path
for root, dirs, files in os.walk(root_path):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

# run
canvas.mainloop()
