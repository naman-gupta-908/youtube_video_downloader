# required libraries
import youtube_dl
import tkinter as tk

# output folder
opts = {'outtmpl':'./videos/%(title)s.%(ext)s'}


def ytdl(x):
    with youtube_dl.YoutubeDL(opts) as y:
        t = y.download([x])


def ytl():
    v = url.get()
    url.delete(0,"end")
    if len(v) != 0:
        ytdl(v)
    else:
        print("not done!!")


box = tk.Tk()
box.title("Youtube downloader")
box.geometry('300x150')
box.configure(bg='#c4302b')

# creating a label for link using widget Label
link_label = tk.Label(box, text = 'Enter the youtube url below : ', font=('Aerial',15, 'bold'),bg='#c4302b')
link_label.pack(padx=10,pady=10)

url = tk.Entry(box,font = ('calibre',15,'normal'))
url.pack(padx=10,pady=10)


down = tk.Button(box, text="Download", command = ytl,font = ('calibre',15,'bold'),bg='#c4302b')
down.pack(padx=10,pady=10)
box.mainloop()
