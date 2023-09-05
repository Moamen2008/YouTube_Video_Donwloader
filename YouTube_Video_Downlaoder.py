from pytube import YouTube

print("Made by Moamen Ashraf\nVideo Downloader V0.1")

link = str(input("Paste Video link over here: "))
yt = YouTube(link)
Res = str(input("res of the video (144p,360p,720p,audio_only) :"))

print("Title: ", yt.title)
print("Views: ", yt.views)



if Res == "144p":
   video = yt.streams.get_lowest_resolution()
   yt_size = yt.streams.get_lowest_resolution().filesize_mb
   print("video-size= ", yt_size)
   ask_downloading = str(input("Do you Want To download the video (y/n)? : "))
   if ask_downloading.lower == "y":
       print("**********!Donwloading!**********")
       video.download()
   else:
       print("thanks for using my program")
elif Res == "240p":
    print("Res not Supported")
elif Res == "360p":
    yt.streams.get_by_resolution("360p").download("Users\Moame\Videos\Pytube\360p")
elif Res == "480p":
    print("Res not Supported")
elif Res == "720p":
    yt.streams.get_highest_resolution().download()
elif Res.lower() == "audio_only" or "audio":
    yt.streams.get_audio_only().download()

print("Done!")