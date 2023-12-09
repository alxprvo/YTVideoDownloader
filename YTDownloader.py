from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import pathlib

# Takes the link passed through the first argument.
link = argv[1]

# Folder path where the video is downloaded.
output_path = pathlib.PureWindowsPath(fr"{pathlib.Path.home()}\Videos\Youtube Downloads")


# Callback function when the download is complete.
def on_complete(strm, file_path):
    print()
    print()
    print("Video downloaded")
    print(file_path.replace('\\', '/'))  # print the path and change the \ to /
    print()


# Create YouTube object. Set progress and complete callback functions.
yt = YouTube(link, on_progress_callback=on_progress, on_complete_callback=on_complete)

# Create stream object at the highest resolution possible.
stream = yt.streams.get_highest_resolution()

print()
print("Title: " + yt.title)
print()

# Download to desired location
stream.download(output_path.as_posix())
