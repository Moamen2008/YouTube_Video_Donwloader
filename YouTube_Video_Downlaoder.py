from pytube import YouTube
from pytube.cli import on_progress 
import time
import subprocess
import easygui

print("Made by Moamen Ashraf\nVideo Downloader V1.00")

try:
     open_folder = open('Path.txt','r')
     path = open_folder.readline()
     open_folder.close()

except FileNotFoundError:
          
     open_folder = open('Path.txt','w+')
     select_path = easygui.diropenbox("Select The Folder You Want To Donwload The Videos In")
     open_folder.write(select_path)
     print("if you want to edit it just edit it inside the path.txt")
     open_folder.close()
     open_folder = open('Path.txt','r')
     path = open_folder.readline()
     open_folder.close()
def main():

          while True:
          
               link = str(input("Paste Video link over here: "))
               if "www.youtube.com/watch?v=" in link:
                    break
               elif "youtu.be" in link :
                    break
               elif "youtube.com/shorts" in link:
                    break
               else:
                    print("Wrong Input")

          yt = YouTube(link, on_progress_callback=on_progress)

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
          video_length = yt.length
          seconds = video_length % 60
          minutes = int(video_length / 60) % 60
          hours = int(video_length / 3600)
          print(f"video length: {hours:02}:{minutes:02}:{seconds:02}")
          
          def video_donwloading():

               def files_videos_extiontions():
                    video_extensions = ["mp4","mkv","avi","webm","m4v","mov"]

                    while True:
                         File_extension = input("chooose file extintion (mp4, mkv, avi, webm, m4v, mov):").lower()
                         if File_extension.lower() in video_extensions:
                              return File_extension
                         else:
                              print("Wrong Input")

               def files_audio_extiontions():
                    audio_extensions = ["mp3", "wav", "flac", "aac", "ogg", "m4a"]

                    while True:
                         File_extension = input("chooose file extintion (mp3, wav, flac, aac, ogg, m4a):").lower()
                         if File_extension.lower() in audio_extensions:
                              return File_extension
                         else:
                              print("Wrong Input")
                         
                    
               if Res == "144p":

                    Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                    if Video_Title.lower() == "title":
                         Video_Title = yt.title

                    File_extension = files_videos_extiontions()
                    
                         
                    print("**********!Donwloading!**********")

                    yt.streams.get_lowest_resolution().download(f"{path}\\144p", filename=f"{Video_Title}.{File_extension}")
                    print("Done!\nFolder Is Opening")
                    time.sleep(1.5)
                    subprocess.run(['explorer', '/select,', f"{path}\\144p\{Video_Title}.{File_extension}"], shell=True)

               elif Res == "360p":

                    Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                    if Video_Title.lower() == "title":
                         Video_Title = yt.title

                    File_extension = files_videos_extiontions()

                    print("**********!Donwloading!**********")

                    yt.streams.get_by_resolution("360p").download(f"{path}\\360p", filename=f"{Video_Title}.{File_extension}")
                    print("Done!\nFolder Is Opening")
                    time.sleep(1.5)
                    subprocess.run(['explorer', '/select,', f"{path}\\360p\{Video_Title}.{File_extension}"], shell=True)

               elif Res == "720p":

                    Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                    if Video_Title.lower() == "title":
                         Video_Title = yt.title

                    File_extension = files_videos_extiontions()

                    print("**********!Donwloading!**********")

                    yt.streams.get_highest_resolution().download(f"{path}\\720p", filename=f"{Video_Title}.{File_extension}")
                    print("Done!\nFolder Is Opening")
                    time.sleep(1.5)
                    subprocess.run(['explorer', '/select,', f"{path}\\720p\{Video_Title}.{File_extension}"], shell=True)

               elif Res.lower() == "audio_only" or "audio":

                    Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                    if Video_Title.lower() == "title":
                         Video_Title = yt.title

                    File_extension = files_audio_extiontions()

                    print("**********!Donwloading!**********")

                    yt.streams.get_audio_only().download(f"{path}\\Audio", filename=f"{Video_Title}.{File_extension}")
                    print("Done!\nFolder Is Opening")
                    time.sleep(1.5)
                    subprocess.run(['explorer', '/select,', f"{path}\Audio\{Video_Title}.{File_extension}"], shell=True)

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
                         time.sleep(1.5)
                         quit()
                         
                    else:
                         print("Please input (y/n) only?")


          if Res == "144p":

               yt_size = yt.streams.get_lowest_resolution().filesize_mb
               print("video-size= ", yt_size,"MB")
               donwload_the_video() 

          elif Res == "360p":

               yt_size = yt.streams.get_by_resolution("360p").filesize_mb
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