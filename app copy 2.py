from pytube import YouTube

link_url = input("\nWrite youtube video url: ")

yt = YouTube(link_url)

for stream in yt.streams:
    print(stream)

# for stream in yt.streams.filter(adaptive=True):
#     print(stream)