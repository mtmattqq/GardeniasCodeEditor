from customtkinter import *
import ssl
from threading import Thread
from pytube import YouTube

ssl._create_default_https_context = ssl._create_stdlib_context

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

app = CTk()
center_window(app, 800, 600)
app.resizable(False, False)
app.title("Youtube Downloader")

set_appearance_mode("dark")
set_default_color_theme("blue")

def on_progress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total

    state.configure(text='Downloading...')
    label.configure(text=f'{percent*100:.0f} %')
    pgbar.set(percent)

def on_complete(stream, file_path):
    state.configure(text='Complete!')
    pgbar.set(1)
    btn.configure(state=NORMAL)

def download(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
        yt.streams.filter().get_highest_resolution().download(output_path='download/')
    except:
        state.configure(text='Invalid URL', text_color='#cc2222')
        btn.configure(state=NORMAL)

def start_download():
    url = entry.get()
    entry.delete(0, END)

    label.configure(text='0 %')
    state.configure(text='Starting...', text_color='#bbbbbb')
    pgbar.set(0)
    btn.configure(state=DISABLED)
    
    download_thread = Thread(target=download, args=(url,))
    download_thread.start()

title = CTkLabel(master=app, text="Youtube Downloader", font=(None, 32), text_color='#bbbbbb')
title.place(relx=0.5, rely=0.15, anchor="center")

footer = CTkLabel(master=app, text="Created by HyperSoWeak", font=(None, 16), text_color='#888888')
footer.place(relx=0.5, rely=0.9, anchor="center")

label = CTkLabel(master=app, text="0 %", font=(None, 20), text_color='#bbbbbb')
label.place(relx=0.72, rely=0.35, anchor="w")

state = CTkLabel(master=app, text="Idle", font=(None, 20), text_color='#bbbbbb')
state.place(relx=0.28, rely=0.35, anchor="e")

pgbar = CTkProgressBar(
    master = app,
    width = 300,
    height = 15,
    border_width = 2
)
pgbar.set(0)
pgbar.place(relx=0.5, rely=0.35, anchor="center")

entry = CTkEntry(
    master = app,
    width = 500,
    height = 40,
    font = (None, 20),
    placeholder_text = "Enter video URL..."
)
entry.place(relx=0.5, rely=0.5, anchor="center")

btn = CTkButton(
    master = app,
    width = 150,
    height = 50,
    font = (None, 25),
    text = "Download",
    command = start_download
)
btn.place(relx=0.5, rely=0.7, anchor="center")

download_thread = None
app.mainloop()