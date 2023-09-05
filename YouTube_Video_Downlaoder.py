from pytube import YouTube
import time
import subprocess

print("Made by Moamen Ashraf\nVideo Downloader V0.7")

def main():
     
     while True:
          
          link = str(input("Paste Video link over here: "))
          if "www.youtube.com/watch?v=" in link:
               break
          elif "youtu.be" in link :
               break
          elif "youtube.com/shorts" in link :
               break
          else:
               print("Wrong Input")

     yt = YouTube(link)
     while True:
          Res = str(input("Res of the Video ( 144p, 360p, 720p, Audio ) ? : ").lower())
          Supported_Res = ["144p", "360p", "720p", "audio", "audio_only"]
          UnSupported_Res = ["240p", "480p", "1080p", "2k", "4k", "2160p", "1440p", "900p", "560p", "180p"]
          if Res in Supported_Res :
               break
          elif Res in UnSupported_Res:
               print("Sorry not supported resolution")
          else:
               print("Wrong Input") 

     print("Title: ", yt.title)
     print("Author: ", yt.author)
     print("Views: ", yt.views)
     print("Time of the video in minutes : ", str(float(yt.length)/60))

     def video_donwloading():

          if Res == "144p":

               Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
               if Video_Title.lower() == "title":
                    Video_Title = yt.title
               
               while True:

                    File_extension = input("chooose file extintion (mp4, mkv, avi, webm):").lower()
                    video_extensions = ["mp4","mkv","avi","webm"]
                    if File_extension.lower() in video_extensions:
                         break
                    elif File_extension.lower() not in video_extensions:
                         print("Wrong Input")
                    else:
                         print("Wrong Input")
                    
               print("**********!Donwloading!**********")

               yt.streams.get_lowest_resolution().download("F:\YoutubeDownload\\144p", filename=f"{Video_Title}.{File_extension}")
               print("Done!\nFolder Is Opening")
               time.sleep(1.5)
               subprocess.run(['explorer', '/select,', f"F:\YoutubeDownload\\144p\{Video_Title}.{File_extension}"], shell=True)

          elif Res == "360p":

               Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
               if Video_Title.lower() == "title":
                    Video_Title = yt.title

               while True:
                    File_extension = input("chooose file extintion (mp4, mkv, avi, webm):")
                    video_extensions = ["mp4","mkv","avi","webm"]
                    if File_extension.lower() in video_extensions:
                         break
                    elif File_extension.lower() not in video_extensions:
                         print("Wrong Input")
                    else:
                         print("Wrong Input")

               print("**********!Donwloading!**********")

               yt.streams.get_by_resolution("360p").download("F:\YoutubeDownload\\360p", filename=f"{Video_Title}.{File_extension}")
               print("Done!\nFolder Is Opening")
               time.sleep(1.5)
               subprocess.run(['explorer', '/select,', f"F:\YoutubeDownload\\360p\{Video_Title}.{File_extension}"], shell=True)

          elif Res == "720p":

               Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
               if Video_Title.lower() == "title":
                    Video_Title = yt.title

               while True:

                    File_extension = input("chooose file extintion (mp4, mkv, avi, webm):")
                    video_extensions = ["mp4","mkv","avi","webm"]
                    if File_extension.lower() in video_extensions:
                         break
                    elif File_extension.lower() not in video_extensions:
                         print("Wrong Input")
                    else:
                         print("Wrong Input")

               print("**********!Donwloading!**********")

               yt.streams.get_highest_resolution().download("F:\YoutubeDownload\\720p", filename=f"{Video_Title}.{File_extension}")
               print("Done!\nFolder Is Opening")
               time.sleep(1.5)
               subprocess.run(['explorer', '/select,', f"F:\YoutubeDownload\\720p\{Video_Title}.{File_extension}"], shell=True)

          elif Res.lower() == "audio_only" or "audio":

               Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
               if Video_Title.lower() == "title":
                    Video_Title = yt.title

               print("**********!Donwloading!**********")

               yt.streams.filter(only_audio=True).first().download("F:\YoutubeDownload\\Audio", filename=f"{Video_Title}.mp3")
               print("Done!\nFolder Is Opening")
               time.sleep(1.5)
               subprocess.run(['explorer', '/select,', f"F:\YoutubeDownload\\Audio\{Video_Title}.mp3"], shell=True)

          else:
               print("Wrong Input")
     
     def donwload_the_video():

          while True:
               play_again = input("Do you want to download the video? (y/n): ")

               if play_again.lower() == "y":
                    video_donwloading()
                    break

               elif play_again.lower() == "n":
                    print("thanks for using my program")
                    
                    
               else:
                    print("Please input (y/n) only?")


     if Res == "144p":
          yt_size = yt.streams.get_lowest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          donwload_the_video() 

     elif Res == "360p":
          yt_size = yt.streams.get_lowest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          donwload_the_video() 

     elif Res == "720p":
          yt_size = yt.streams.get_highest_resolution().filesize_mb
          print("video-size= ", yt_size,"MB")
          donwload_the_video()  

     elif Res.lower() == "audio_only":
          yt_size = yt.streams.get_audio_only().filesize_mb
          print("video-size= ", yt_size,"MB")
          donwload_the_video() 

     elif Res.lower() == "audio":
          yt_size = yt.streams.get_audio_only().filesize_mb
          print("video-size= ", yt_size,"MB")
          donwload_the_video() 


def main_use():
     main()
     while True:
          re_use = input("Do You Want To Download Another Video (y/n)? : ")
          if re_use == "y":
               main_use()
          elif re_use == "n":
               print("Thank You For Using My Program")
               time.sleep(3)
               quit()
          else:
               print("Please input (y/n) only?")
main_use()