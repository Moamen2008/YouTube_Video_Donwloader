from pytube import YouTube
from pytube import Playlist
import time
import subprocess
import easygui

print("Made by Moamen Ashraf\nVideo Downloader V1.10")

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
    PL_Link_input = input("Please input The link: ")
    if "www.youtube.com/playlist?list=" in PL_Link_input:
        break
    else:
        print("Wrong Input")


  PL_Link = Playlist(PL_Link_input)
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

          def remove_special_characters(input_string):
            if '|' in input_string or '\\' in input_string or '/' in input_string:
                cleaned_string = input_string.replace('|', '').replace('\\', '').replace('/', '')
                return cleaned_string
            else:
                return input_string
            
          input_string = PL_Link.title
          cleaned_playlist = remove_special_characters(input_string)
                      
          if Res == "144p":
              File_extension = files_videos_extiontions()
                    
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
              File_extension = files_videos_extiontions()

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
              File_extension = files_videos_extiontions()

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

          elif Res.lower() == "audio_only" or "audio":
              File_extension = files_audio_extiontions()

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

  if Res == "144p":
    for yt_in_pl in PL_Link:
        yt_size = YouTube(yt_in_pl).streams.get_lowest_resolution().filesize_mb
        all_yt_sizes = all_yt_sizes + yt_size
    print(f"Playlist_size= {all_yt_sizes} MB" )
    donwload_the_video()
    
  elif Res == "360p":
     for yt_in_pl in PL_Link:
        yt_size = YouTube(yt_in_pl).streams.get_lowest_resolution().filesize_mb
        all_yt_sizes = all_yt_sizes + yt_size
     print(f"Playlist_size= {all_yt_sizes} MB" )
     donwload_the_video() 

  elif Res == "720p":

    for yt_in_pl in PL_Link:
        yt_size = YouTube(yt_in_pl).streams.get_highest_resolution().filesize_mb
        all_yt_sizes = all_yt_sizes + yt_size
    print(f"Playlist_size= {all_yt_sizes} MB" )
    donwload_the_video() 

  elif Res.lower() == "audio_only":
     for yt_in_pl in PL_Link:
        yt_size = YouTube(yt_in_pl).streams.get_audio_only().filesize_mb
        all_yt_sizes = all_yt_sizes + yt_size
     print(f"Playlist_size= {all_yt_sizes} MB" )
     donwload_the_video() 

  elif Res.lower() == "audio":
      for yt_in_pl in PL_Link:
        yt_size = YouTube(yt_in_pl).streams.get_audio_only().filesize_mb
        all_yt_sizes = all_yt_sizes + yt_size
      print(f"Playlist_size= {all_yt_sizes} MB" )
      donwload_the_video() 

main()