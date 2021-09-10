#pytube, GUI libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

from pytube import YouTube

#root window design
root = Tk()
root.configure(bg='#434343')
root.geometry('738x506')
root.minsize(738, 506)
root.maxsize(738, 506)

root.title('HM DOWNLOADER')
root.iconbitmap('icon.ico')

logoImage = ImageTk.PhotoImage(Image.open('logo.png'))
logoLabel = Label(image=logoImage, bg='#434343')
logoLabel.grid(row=1, column=1, padx=10, pady=0, columnspan=2)

frameLeft = LabelFrame(root, text='Stream', padx=50, pady=56, bg='#434343', fg='#fe8d36', font='Helvetica 9 bold')
frameLeft.grid(row=2, column=1, padx=10, pady=0)

frameRight = LabelFrame(root, text='Quality', padx=50, pady=50, bg='#434343', fg='#fe8d36', font='Helvetica 9 bold')
frameRight.grid(row=2, column=2, padx=0, pady=0)


#Entery, GUI - link
linkLabel = Label(frameLeft, text='Link', bg='#434343', fg='#ffffff', font='Helvetica 9 bold')
linkLabel.grid(row=1, column=1, padx=5, pady=10)

urlEntry = Entry(frameLeft, width=50, borderwidth=0)
urlEntry.grid(row=1, column=2, padx=10, pady=10)


#Entery, GUI - path
savePath = StringVar()

pathLabel = Label(frameLeft, text='Path', bg='#434343', fg='#ffffff', font='Helvetica 9 bold')
pathLabel.grid(row=2, column=1, padx=5, pady=10)

pathEntry = Entry(frameLeft, text=savePath, width=50, borderwidth=0)
pathEntry.grid(row=2, column=2, padx=10, pady=10)


#stream quality function
quastm = IntVar()
quastm.set(22)
itag = 22

def func_quality(value):
    global itag
    itag = str(value)

    return 0
button720p = Radiobutton(frameRight, text='720p', variable=quastm, value=22, command=lambda: func_quality(quastm.get()), bg='#434343', fg='#fe8d36', font='Helvetica 9 bold').pack()
button360p = Radiobutton(frameRight, text='360p', variable=quastm, value=18, command=lambda: func_quality(quastm.get()), bg='#434343', fg='#fe8d36', font='Helvetica 9 bold').pack()
button1440p = Radiobutton(frameRight, text='144p', variable=quastm, value=17, command=lambda: func_quality(quastm.get()), bg='#434343', fg='#fe8d36', font='Helvetica 9 bold').pack()
buttonAudio = Radiobutton(frameRight, text='Audio', variable=quastm, value=251, command=lambda: func_quality(quastm.get()), bg='#434343', fg='#fe8d36', font='Helvetica 9 bold').pack()


#browse directory function
def func_browse():
    global savePath
    PATH = filedialog.askdirectory()
    savePath.set(PATH)

    return 0
browseButton = Button(frameLeft, text='Browse', command=func_browse, bg='#434343', fg='#ffffff', font='Helvetica 9 bold')
browseButton.grid(row=2, column=3, padx=10, pady=10)


#progress register function
def func_progress(chunk, fh, bytes_remaining):
    global dProgress
    streamSize = stream.filesize
    dProgress = int(((streamSize - bytes_remaining) / streamSize) * 100)


#completion register function
def func_complete(self, file_path):
    messagebox.showinfo('Status', 'Download Complete!')


#pytube download function >>[itag - from func_quality(), URL, dLocation]<<
def func_download():
    global stream

    URL = urlEntry.get()
    dLocation = pathEntry.get()

    yt = YouTube(str(URL), on_progress_callback=func_progress, on_complete_callback=func_complete)
    stream = yt.streams.get_by_itag(int(itag))
    stream.download(str(dLocation))

    return 0
downloadButton = Button(root, text='Download', command=func_download, bg='#fe8d36', fg='#ffffff', font='Helvetica 13 bold', height=1, width=25)
downloadButton.grid(row=3, column=1, columnspan=2, pady=25)

root.mainloop()