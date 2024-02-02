from pytube import YouTube

def download(video_resolutions, videos):
    while True:
        # Looping through the video_resolutions list to be displayed on the screen for user selection...
        i = 1
        for resolution in video_resolutions:
            print(f'{i}. {resolution}')
            i += 1

        # To Download the video with the users Choice of resolution
        choice = int(input('\nChoose A Resolution Please: '))
        
        # To validate if the user enters a number displayed on the screen...
        if 1 <= choice < i:
            resolution_to_download = video_resolutions[choice - 1]
            print(f"You're now downloading the video with resolution {resolution_to_download}...")

            # command for downloading the video
            videos[choice - 1].download()

            print("\nVideo was successfully downloaded!")
            break

        else:
            print("Invalid choice!!\n\n")


def sort_resolutions(url):
    # URL (user input)
    my_video = YouTube(url)
    print(my_video.title)
    # Title of The Video

    # Now for the Thumbnail Image
    print("Thumbnail URL")
    print(my_video.thumbnail_url)

    video_resolutions = []
    videos = []

    for stream in my_video.streams.order_by('resolution'):
        # print(stream)
        video_resolutions.append(stream.resolution)
        videos.append(stream)

    # print(video_resolutions)

    return video_resolutions, videos


print("Please Paste The URL of the youtube video")
url = "https://www.youtube.com/watch?v=KKmLh9rNybI"

video_resolutions, videos = sort_resolutions(url)

download(video_resolutions, videos)