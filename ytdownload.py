from pytube import YouTube
import tkinter as tk
import os

window = tk.Tk()
window.resizable(False, False)
window.title("YouTube Downloader")
window.iconphoto(False, tk.PhotoImage(file='F:\programming\PYprojects\YTDownload\ytdownload.png'))
window.configure(bg="lightblue")
w = 800
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

label_link = tk.Label(window)
label_error = tk.Label(window)
label_info = tk.Label(window)
entry_link = tk.Entry(window)
entry_location = tk.Entry(window)
button_downmp4 = tk.Button(window)
button_reset = tk.Button(window)
button_clear = tk.Button(window)


def organize_length(seconds):
    minutes = 0
    hours = 0
    value = ""
    if seconds % 3600 != 0:
        if seconds % 60 != 0:
            if seconds < 60:
                value = str(f"\nLength:\n{hours}h {minutes}m {seconds}s")
            else:
                while seconds % 3600 > 0:
                    if seconds > 3600:
                        seconds -= 3600
                        hours += 1
                        if seconds < 3600:
                            break
                    else:
                        break

                while seconds % 60 > 0:
                    if seconds > 60:
                        seconds -= 60
                        minutes += 1
                        if seconds < 60:
                            break
                value = str(f"\nLength:\n{hours}h {minutes}m {seconds}s")
        else:
            minutes = seconds / 60
            value = str(f"\nLength:\n{hours}h {minutes}m {seconds}s")
    else:
        hours = seconds / 360
        value = str(f"\nLength:\n{hours}h {minutes}m {seconds}s")
    return value


def download_mp4():
    try:
        vid_link = entry_link.get()
        location = entry_location.get()
        yt = YouTube(vid_link)
        if len(entry_location.get()) == 0:
            label_error.configure(justify=tk.LEFT, text="Oops! Something went wrong!")
        else:
            ys = yt.streams.get_highest_resolution()
            ys.download(location)
            entry_link.delete(0, tk.END)
            label_error.configure(justify=tk.LEFT, text="By default your video is downloaded in a folder named Downloads.\nYou will find it where ever you saved your .exe.")
            title = f"Title:\n{yt.title}"
            numviews = f"\nNumber of views:\n{yt.views}"
            len_of_vid = organize_length(yt.length)
            label_info.configure(justify=tk.LEFT, text=f"Information about the video:\n{title}\n{numviews}\n{len_of_vid}", wraplength=300)
    except:
        label_error.configure(justify=tk.LEFT, text="Oops! Something went wrong!")


def reset():
    label_error.configure(justify=tk.LEFT, text="By default your video is downloaded in a folder named Downloads.\nYou will find it where ever you saved your .exe.")
    label_info.configure(justify=tk.LEFT, text="Information about the video:", bg="lightblue")
    entry_link.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_location.insert(1, "Downloads")

def clear():
    entry_link.delete(0, tk.END)
    entry_location.delete(0, tk.END)

def hover(e):
    e.widget.configure(foreground='white')

def unhover(e):
    e.widget.configure(foreground='black')

label_link.configure(justify=tk.LEFT, text="Paste the link here: \n\nPaste the location here:", bg="lightblue")
label_link.place(x=10, y=10)

label_error.configure(justify=tk.LEFT, text="By default your video is downloaded in a folder named Downloads.\nYou will find it where ever you saved your .exe.", bg="lightblue")
label_error.place(x=10, y=110)

label_info.configure(justify=tk.LEFT, text="Information about the video:", bg="lightblue")
label_info.place(x=450, y=10)

entry_link.configure(width=46, foreground="white", background="#3b6275")
entry_link.place(x=140, y=12)

entry_location.insert(1, "Downloads")
entry_location.configure(width=46, foreground="white", background="#3b6275")
entry_location.place(x=140, y=42)

button_downmp4.configure(width= 15, background="#6fb7d9", text="Download MP4", command=lambda: download_mp4())
button_downmp4.place(x=10, y=80)
button_downmp4.bind('<Enter>', hover)
button_downmp4.bind('<Leave>', unhover)

button_reset.configure(width= 10, background="#6fb7d9", text="Reset", command=lambda: reset())
button_reset.place(x=130, y=80)
button_reset.bind('<Enter>', hover)
button_reset.bind('<Leave>', unhover)

button_clear.configure(width= 10, background="#6fb7d9", text="Clear", command=lambda: clear())
button_clear.place(x=215, y=80)
button_clear.bind('<Enter>', hover)
button_clear.bind('<Leave>', unhover)

window.mainloop()