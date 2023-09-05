from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import os
import time
import subprocess
import easygui
import string
import urllib.request

all_letters_lower = list(string.ascii_letters.lower())
all_letters_upper = list(string.ascii_letters.upper())


print("YouTube Video and Playlist Downloader\nMade By Moamen Ashraf V1.00\n{input (Exit) to quit}\n{input (Change) to Change the Path}")

try:
     open_folder = open('Path.txt','r')
     path = open_folder.readline()
     open_folder.close()

except FileNotFoundError:
     open_folder = open('Path.txt','w+')
     select_path = easygui.diropenbox("Select The Folder You Want To Download The Videos In")
     open_folder.write(select_path)
     print("if you want to edit it just edit it inside the path.txt")
     open_folder.close()
     open_folder = open('Path.txt','r')
     path = open_folder.readline()
     open_folder.close()

if not os.path.isdir(path):
    open_folder = open('Path.txt','w+')
    select_path = easygui.diropenbox("Select The Folder You Want To Download The Videos In")
    open_folder.write(select_path)
    print("if you want to edit it just edit it inside the path.txt")
    open_folder.close()
    open_folder = open('Path.txt','r')
    path = open_folder.readline()
    open_folder.close()


def main():
  while True:
          
    link = str(input("Paste link over here: "))
    if "www.youtube.com/watch?v=" in link:
        Video_Main(link)
    elif "youtu.be" in link :
        Video_Main(link)
    elif "youtube.com/shorts" in link:
        Video_Main(link)
    elif "www.youtube.com/playlist?list=" in link:
        Playlist_Main(link)
    elif "exit" == link.lower() or "(exit)" == link.lower():
        print("Thank You For Using My Program")
        time.sleep(1)
        quit()
    elif "change" == link.lower() or "(change)" == link.lower():
        open_folder = open('Path.txt','w+')
        select_path = easygui.diropenbox("Select The Folder You Want To Download The Videos In")
        open_folder.write(select_path)
        print("if you want to edit it just edit it inside the path.txt")
        open_folder.close()
        open_folder = open('Path.txt','r')
        path = open_folder.readline()
        open_folder.close()
        main()
    else:
        print("Wrong Input")

def Video_Main(link):
      yt = YouTube(link, on_progress_callback=on_progress)

      Supported_Res = ["144p", "360p", "720p", "audio", "audio_only", "thumbnail"]
      UnSupported_Res = ["240p", "480p", "1080p", "2k", "4k", "2160p", "1440p", "900p", "560p", "180p"]
      while True:
          Res = str(input("Res of the Video ( 144p, 360p, 720p, Audio, Thumbnail ) ? : ").lower())
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

            def files_videos_extensions():
                video_extensions = ["mp4","mkv","avi","webm","m4v","mov"]

                while True:
                      File_extension = input("chooose file extension (mp4, mkv, avi, webm, m4v, mov):").lower()
                      if File_extension.lower() in video_extensions:
                          return File_extension
                      else:
                          print("Wrong Input")

            def files_audio_extensions():
                audio_extensions = ["mp3", "wav", "flac", "aac", "ogg", "m4a"]

                while True:
                      File_extension = input("chooose file extension (mp3, wav, flac, aac, ogg, m4a):").lower()
                      if File_extension.lower() in audio_extensions:
                          return File_extension
                      else:
                          print("Wrong Input")

            def remove_special_characters(input_string):
              if '|' in input_string or '\\' in input_string or '/' in input_string:
                  cleaned_string = input_string.replace('|', '').replace('\\', '').replace('/', '')
                  return cleaned_string
              else:
                  return input_string
            input_string = yt.title
            cleaned_Video = remove_special_characters(input_string)

            if Res.lower() == "thumbnail":
                if not os.path.exists(path + "\\Thumbnails"):
                    os.makedirs(path + "\\Thumbnails")
                url = yt.thumbnail_url
                full_path = os.path.join(path +"\\"+"Thumbnails\\"+ cleaned_Video + '.jpg')
                urllib.request.urlretrieve(url, full_path)
                subprocess.run(['explorer', '/select,', f"{path}\Thumbnails\{cleaned_Video}.jpg"], shell=True)
            elif Res == "144p":

                Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                if Video_Title.lower() == "title":
                      Video_Title = cleaned_Video

                File_extension = files_videos_extensions()
                
                      
                print("**********!Donwloading!**********")

                yt.streams.get_lowest_resolution().download(f"{path}\\144p", filename=f"{Video_Title}.{File_extension}")
                print("Done!\nFolder Is Opening")
                time.sleep(1.5)
                subprocess.run(['explorer', '/select,', f"{path}\\144p\{Video_Title}.{File_extension}"], shell=True)

            elif Res == "360p":

                Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                if Video_Title.lower() == "title":
                      Video_Title = cleaned_Video

                File_extension = files_videos_extensions()

                print("**********!Donwloading!**********")

                yt.streams.get_by_resolution("360p").download(f"{path}\\360p", filename=f"{Video_Title}.{File_extension}")
                print("Done!\nFolder Is Opening")
                time.sleep(1.5)
                subprocess.run(['explorer', '/select,', f"{path}\\360p\{Video_Title}.{File_extension}"], shell=True)

            elif Res == "720p":

                Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                if Video_Title.lower() == "title":
                      Video_Title = cleaned_Video

                File_extension = files_videos_extensions()

                print("**********!Donwloading!**********")

                yt.streams.get_highest_resolution().download(f"{path}\\720p", filename=f"{Video_Title}.{File_extension}")
                print("Done!\nFolder Is Opening")
                time.sleep(1.5)
                subprocess.run(['explorer', '/select,', f"{path}\\720p\{Video_Title}.{File_extension}"], shell=True)

            elif Res.lower() == "audio_only" or Res.lower() == "audio":

                Video_Title = input("please Input Video Title (Write Title if you want the same video title): ")
                if Video_Title.lower() == "title":
                      Video_Title = cleaned_Video

                File_extension = files_audio_extensions()

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

      if Res.lower() == "thumbnail":
                video_donwloading()

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
  
def Playlist_Main(link):
       
      PL_Link = Playlist(link)
      Supported_Res = ["144p", "360p", "720p", "audio", "audio_only", "thumbnail"]
      UnSupported_Res = ["240p", "480p", "1080p", "2k", "4k", "2160p", "1440p", "900p", "560p", "180p"]
      while True:
          Res = str(input("Res of the Video ( 144p, 360p, 720p, Audio, Thumbnail ) ? : ").lower())
          if Res in Supported_Res :
              break
          elif Res in UnSupported_Res:
              print("Sorry not supported resolution")
          else:
              print("Wrong Input")
      print("Title: ", PL_Link.title)
      print("Author: ", PL_Link.owner)
      print("Views: ",  PL_Link.views)
      all_videos_length = 0
      for video in PL_Link:
        yt = YouTube(video)
        video_length = yt.length
        all_videos_length = video_length + all_videos_length
      seconds = all_videos_length % 60
      minutes = int(all_videos_length / 60) % 60
      hours = int(all_videos_length / 3600)
      print(f"video length: {hours:02}:{minutes:02}:{seconds:02}")

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


      def video_donwloading():
              Downloaded_videos = 0
              def files_videos_extensions():
                        video_extensions = ["mp4","mkv","avi","webm","m4v","mov"]

                        while True:
                            File_extension = input("chooose file extension (mp4, mkv, avi, webm, m4v, mov):").lower()
                            if File_extension.lower() in video_extensions:
                                  return File_extension
                            else:
                                  print("Wrong Input")

              def files_audio_extensions():
                        audio_extensions = ["mp3", "wav", "flac", "aac", "ogg", "m4a"]

                        while True:
                            File_extension = input("chooose file extension (mp3, wav, flac, aac, ogg, m4a):").lower()
                            if File_extension.lower() in audio_extensions:
                                  return File_extension
                            else:
                                  print("Wrong Input")

              def remove_special_characters(input_string):
                if '|' in input_string or '\\' in input_string or '/' in input_string:
                    cleaned_string = input_string.replace('|', '').replace('\\', '').replace('/', '')
                    return cleaned_string
                else:
                    return input_string
                
              input_string = PL_Link.title
              cleaned_playlist = remove_special_characters(input_string)
              

              if Res.lower() == "thumbnail":
                Downloaded_thumbnails = 0
                if not os.path.exists(path + "\\Thumbnails"+"\\"+cleaned_playlist):
                    os.makedirs(path + "\\Thumbnails"+"\\"+cleaned_playlist)
                for video in PL_Link:
                    Downloaded_thumbnails += 1
                    cleaned_Video = remove_special_characters(YouTube(video).title)
                    url = YouTube(video).thumbnail_url
                    full_path = os.path.join(path +"\\"+"Thumbnails\\"+cleaned_playlist+"\\"+ cleaned_Video + '.jpg')
                    urllib.request.urlretrieve(url, full_path)
                    print(f"{cleaned_Video} Thumbnail Downloaded, {Downloaded_thumbnails} Thumbnail Done")
                print("Done!\nFolder Is Opening")
                time.sleep(1.5)
                subprocess.run(['explorer', f"{path}\Thumbnails\{cleaned_playlist}"])        
              elif Res == "144p":
                  File_extension = files_videos_extensions()
                        
                  print("**********!Donwloading!**********")

                  for video in PL_Link:
                    input_string = YouTube(video).title
                    cleaned_string = remove_special_characters(input_string)
                    YouTube(video).streams.get_lowest_resolution().download(f"{path}\{cleaned_playlist}", filename=f"{cleaned_string}.{File_extension}")
                    Downloaded_videos = Downloaded_videos + 1
                    print(f"{cleaned_string} Downloaded, {Downloaded_videos} Video Done")
                  print("Done!\nFolder Is Opening")
                  time.sleep(1.5)
                  subprocess.run(['explorer', f"{path}\{cleaned_playlist}"])

              elif Res == "360p":
                  File_extension = files_videos_extensions()

                  print("**********!Donwloading!**********")
                  for video in PL_Link:
                    input_string = YouTube(video).title
                    cleaned_string = remove_special_characters(input_string)
                    YouTube(video).streams.get_by_resolution("360p").download(f"{path}\{cleaned_playlist}", filename=f"{cleaned_string}.{File_extension}")
                    Downloaded_videos = Downloaded_videos + 1
                    print(f"{cleaned_string} Downloaded, {Downloaded_videos} Video Done")
                  print("Done!\nFolder Is Opening")
                  time.sleep(1.5)
                  subprocess.run(['explorer', f"{path}\{cleaned_playlist}"])

              elif Res == "720p":
                  File_extension = files_videos_extensions()

                  print("**********!Donwloading!**********")
                  for video in PL_Link:
                    input_string = YouTube(video).title
                    cleaned_string = remove_special_characters(input_string)
                    YouTube(video).streams.get_highest_resolution().download(f"{path}\{cleaned_playlist}", filename=f"{cleaned_string}.{File_extension}")
                    Downloaded_videos = Downloaded_videos + 1
                    print(f"{cleaned_string} Downloaded, {Downloaded_videos} Video Done")
                  print("Done!\nFolder Is Opening")
                  time.sleep(1.5)
                  subprocess.run(['explorer', f"{path}\{cleaned_playlist}"])

              elif Res.lower() == "audio_only" or Res.lower() == "audio":
                  File_extension = files_audio_extensions()

                  print("**********!Donwloading!**********")
                  for video in PL_Link:
                    input_string = YouTube(video).title
                    cleaned_string = remove_special_characters(input_string)
                    YouTube(video).streams.get_audio_only().download(f"{path}\{cleaned_playlist}", filename=f"{cleaned_string}.{File_extension}")
                    Downloaded_videos = Downloaded_videos + 1
                    print(f"{cleaned_string} Downloaded, {Downloaded_videos} Video Done")
                  print("Done!\nFolder Is Opening")
                  time.sleep(1.5)
                  subprocess.run(['explorer', f"{path}\{cleaned_playlist}"])

              else:
                  print("Wrong Input")
          
      all_yt_sizes = 0
      
      if Res.lower() == "thumbnail":
                video_donwloading()

      if Res == "144p":
        print("Don't Panic if it takes time it's getting the size of the playlist")
        for yt_in_pl in PL_Link:
            yt_size = YouTube(yt_in_pl).streams.get_lowest_resolution().filesize_mb
            all_yt_sizes = all_yt_sizes + yt_size
        print(f"Playlist_size= {all_yt_sizes} MB" )
        donwload_the_video()
        
      elif Res == "360p":
        print("Don't Panic if it takes time it's getting the size of the playlist")
        for yt_in_pl in PL_Link:
            yt_size = YouTube(yt_in_pl).streams.get_lowest_resolution().filesize_mb
            all_yt_sizes = all_yt_sizes + yt_size
        print(f"Playlist_size= {all_yt_sizes} MB" )
        donwload_the_video() 

      elif Res == "720p":
        print("Don't Panic if it takes time it's getting the size of the playlist")
        for yt_in_pl in PL_Link:
            yt_size = YouTube(yt_in_pl).streams.get_highest_resolution().filesize_mb
            all_yt_sizes = all_yt_sizes + yt_size
        print(f"Playlist_size= {all_yt_sizes} MB" )
        donwload_the_video() 

      elif Res.lower() == "audio_only" or Res.lower() == "audio" :
        print("Don't Panic if it takes time it's getting the size of the playlist")
        for yt_in_pl in PL_Link:
            yt_size = YouTube(yt_in_pl).streams.get_audio_only().filesize_mb
            all_yt_sizes = all_yt_sizes + yt_size
        print(f"Playlist_size= {all_yt_sizes} MB" )
        donwload_the_video()
          
main()