from pytube import YouTube
import customtkinter as ctk
from tkinter import ttk
import os

def download_video():
    url = entry_url.get()

    progress_bar.pack()
    progress_label.pack()
    status_label.pack()

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream=yt.streams.filter(progressive=True).get_highest_resolution()

        #download video into a specific directory
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")

        status_label.configure(text=f"Downloaded", text_color="white", fg_color="green")
    except Exception as e:
        status_label.configure (text=f"Woops, some problem: {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    
    progress_label.configure(text = str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))

#create root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#title of the window
root.title("Youtube Downloader")

#set min and max width and height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)

#create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=10)

#create a label and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")
# progress_label.pack()

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

#create status label
status_label = ctk.CTkLabel(content_frame, text="")

#to start the app
root.mainloop()