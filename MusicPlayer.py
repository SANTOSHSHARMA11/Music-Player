from tkinter import *
from tkinter import colorchooser
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
import os
from mutagen.mp3 import MP3
import time
import threading

root = Tk()
root.resizable(0, 0)
mixer.init()


# ...............................Frame


def browse_music():
	global file
	file = filedialog.askopenfilename()


def color_choose():
	global clr
	clr = colorchooser.askcolor(title="Select Theme")
	root.configure(bg=clr[1])
	print(id(clr))


frame = Frame(root, bg="#FFEFD5")
frame.pack(padx=90, pady=20)

fr = Frame(root, bg="#FFEFD5")
fr.pack()


# frame.configure(bg=clr[1])


def about_us():
	messagebox.showinfo("MusicPlayer",
						"Developer= SANTOSH.H.SHARMA \nVersion = 0.0.1.1 \nCompany_Name = Ramanand Arya " "D.A.V \nTechnology = PYTHON   3.8 \nCopyright by SANTOSH 2020-2030")


# ..........................MenuBar
menubar = Menu(root, bg="#FFEFD5")
root.config(menu=menubar, bg="#FFEFD5")
# ...........................SubMenu
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Theme", menu=submenu)
submenu.add_command(label="Theme_UI", command=color_choose)
submenu.add_command(label="Exit", command=root.destroy)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About_Us", command=about_us)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Music", menu=submenu)
submenu.add_command(label="Browse", command=browse_music)


# ...........................Function

def confg():
	# root.geometry('400x250')
	root.title('Player')
	root.configure(bg="#FFEFD5")
	root.iconbitmap("logo.ico")


def play_btn():
	try:
		mixer.music.load(file)
		print(id(file))
		mixer.music.play()
		status['text'] = "Playing" + ':-' + os.path.basename(file)
		song = MP3(file)
		a = song.info.length
		mins, secs = divmod(a, 60)
		mins = round(mins)
		secs = round(secs)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		lenglab['text'] = "Total Length: " + "- " + timeformat
		t1 = threading.Thread(target=curtim, args=(a,))
		t1.start()

	except:
		messagebox.showinfo(" Browse ", "Go To Music & Select Song")


def stop_btn():
	mixer.music.pause()
	status['text'] = "Paused "


def curtim(p):
	while p :
		'''paused = False
		if paused:
			break
		else:'''
		mins, secs = divmod(p, 60)
		mins = round(mins)
		secs = round(secs)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		currtimelab['text'] = "Remaning-Time: " + "- " + timeformat
		time.sleep(1)
		p -= 1


def retry_btn():
	try:
		mixer.music.unpause()
		status['text'] = " Playing " + ':-' + os.path.basename(file)
	except:
		messagebox.showinfo(" Browse ", "Go To Music & Select Song")


def volume_Scale(val):
	volume = int(val) / 100
	mixer.music.set_volume(volume)


muted = FALSE


def mute():
	global muted
	if muted:  # Unmute the music

		volbtn.configure(image=volphoto)
		scale.set(70)
		mixer.music.set_volume(.7)
		muted = FALSE
	else:  # Mute the music
		volbtn.configure(image=mutphoto)
		scale.set(0)
		mixer.music.set_volume(0)
		muted = TRUE


# ..........................Photo
volphoto = PhotoImage(file="noise.png")
mutphoto = PhotoImage(file="silent.png")
Playphoto = PhotoImage(file="ex.png")
Stopphoto = PhotoImage(file="stop.png")
RetryPhoto = PhotoImage(file="retry.png")

# ..........................Command
volbtn = Button(fr, image=volphoto, bg="#FFEFD5", command=mute)
volbtn.grid(row=1, column=0, padx=5)
Playbtn = Button(frame, image=Playphoto, bg="#FFEFD5", command=play_btn)
Playbtn.grid(row=1, column=0, padx=10)
Stopbtn = Button(frame, image=Stopphoto, bg="#FFEFD5", command=stop_btn)
Stopbtn.grid(row=1, column=1, padx=10)
Retrybtn = Button(frame, image=RetryPhoto, bg="#FFEFD5", command=retry_btn)
Retrybtn.grid(row=1, column=3, padx=10)

status = Label(root, text="Welcome To Player", relief=SUNKEN)
status.pack(side=BOTTOM, fill=X, pady=10)

scale = Scale(fr, from_=0, to=100, orient=HORIZONTAL, command=volume_Scale, bg="#FFEFD5")
scale.set(30)
mixer.music.set_volume(.3)
scale.grid(row=1, column=1, padx=5)

lenglab = Label(fr, text="Total-Time: 00:00", bg="#FFEFD5", relief=RAISED)
lenglab.grid(row=2, column=0)

currtimelab = Label(fr, text=" Remaning-Time: 00:00", bg="#FFEFD5", relief=RAISED)
currtimelab.grid(row=2, column=1)

confg()
root.mainloop()
