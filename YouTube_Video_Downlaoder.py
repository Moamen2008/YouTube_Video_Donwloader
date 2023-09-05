from pytube import YouTube
import time

print("Made by Moamen Ashraf \nVideo Downloader V0.3")

def main():

     link = str(input("Paste Video link over here: "))
     yt = YouTube(link)
     Res = str(input("Res of the Video ( 144p, 360p, 720p, Audio ) ? : "))
          

     
     print("Title: ", yt.title)
     print("Author: ", yt.author)
     print("Views: ", yt.views)
     print("Time of the video in minutes : ", str(float(yt.length)/60))

     def video_donwloading():
          print("**********!Donwloading!**********")
     if Res == "144p":
          yt.streams.get_lowest_resolution().download("F:\YoutubeDownload\\144p")
          print("Done!")
     elif Res == "360p":
          yt.streams.get_by_resolution("360p").download("F:\YoutubeDownload\\360p")
          print("Done!")
     elif Res == "720p":
          yt.streams.get_highest_resolution().download("F:\YoutubeDownload\\720p")
          print("Done!")
     elif Res.lower() == "audio_only" or "audio":
          yt.streams.filter(only_audio=True).first().download("F:\YoutubeDownload\\Audio", filename=f"{yt.title}.mp3" )
          print("Done!")
     else:
          print("Wrong Input")
     


     if Res == "144p":
          yt_size = yt.streams.get_lowest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          play_again = input("Do you want to download the video? (y/n): ")
          if play_again.lower() == "y":
               video_donwloading()
          if play_again.lower() == "n":
               print("thanks for using my program") 
               
     elif Res == "240p":
          print("Res not Supported")

     elif Res == "360p":
          yt_size = yt.streams.get_lowest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          play_again = input("Do you want to download the video? (y/n): ")
          if play_again.lower() == "y":
               video_donwloading()
          if play_again.lower() == "n":
               print("thanks for using my program") 

     elif Res == "480p":
          print("Res not Supported")

     elif Res == "720p":
          yt_size = yt.streams.get_highest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          play_again = input("Do you want to download the video? (y/n): ")
          if play_again.lower() == "y":
               video_donwloading()
          if play_again.lower() == "n":
               print("thanks for using my program") 

     elif Res.lower() == "audio_only":
          yt_size = yt.streams.get_audio_only().filesize_mb
          print("video-size= ", yt_size,"MB")
          play_again = input("Do you want to download the video? (y/n): ")
          if play_again.lower() == "y":
               video_donwloading()
          if play_again.lower() == "n":
               print("thanks for using my program") 

     elif Res.lower() == "audio":
          yt_size = yt.streams.get_audio_only().filesize_mb
          print("video-size= ", yt_size,"MB")
          play_again = input("Do you want to download the video? (y/n): ")
          if play_again.lower() == "y":
               video_donwloading()
          if play_again.lower() == "n":
               print("thanks for using my program") 
     else:
          print("Wrong Input")


def main_use():
     main()
     re_use = input("Do You Want To Download Another Video (y/n)? : ")
     if re_use == "y":
          main_use()
     elif re_use == "n":
          print("Thank You For Using My Program")
          time.sleep(3)
          quit()
     
main_use()