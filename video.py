from pytube import YouTube


link = "https://www.youtube.com/watch?v=OCBeBlpVZBY"
yt = YouTube(link)


# try:
#     # object creation using YouTube which was imported in the beginning
#     yt = YouTube(link)
# except:
#     print("Connection Error")  # to handle exception
#
# # filters out all the files with "mp4" extension
# mp4files = yt.streams.filter('mp4')
#
# # yt.set_filename('GeeksforGeeks Video')  # to set the name of the file
#
# # get the video with the extension and resolution passed in the get() function
# d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
# try:
#     # downloading the video
#     d_video.download(SAVE_PATH)
# except:
#     print("Some Error!")
# print('Task Completed!')
for i in yt.streams.filter(progressive=True, file_extension='mp4').all():
    #  print(vars(i))
    # for j in vars(i):
    j = i.__dict__
    if(j.get('fmt_profile').get('resolution') == '720p'):
        stream = i
        break

try:
    stream.download('E:/')
except:
    print('Couldn\'t download video. Please try again')




