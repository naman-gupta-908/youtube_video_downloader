from pytube import YouTube
link=input("Enter Video's URL : ")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
print("video downloaded")
