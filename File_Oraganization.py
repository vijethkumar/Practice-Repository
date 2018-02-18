
Vijeth_Files ="""my.song.mp3 11b
greatSong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""

Vijeth_List=Vijeth_Files.splitlines()
Vijeth_Music=[]
Vijeth_Image=[]
Vijeth_Movie=[]
Vijeth_Other=[]
Music_Size =0
Image_Size =0
Movie_Size =0
Other_Size =0
for i in range(len(Vijeth_List)):
    Vijeth_List[i]=Vijeth_List[i].rstrip()

for i in range(len(Vijeth_List)):
    Vijeth_List[i]=Vijeth_List[i].split(" ")

for i in range(len(Vijeth_List)):
    print(Vijeth_List[i])

# for i in range(len(Vijeth_List)):
#     if Vijeth_List[i][0] == 'my.song.mp3':
#         Vijeth_Music.append(Vijeth_List[i])

for i in range(len(Vijeth_List)):
    Vijeth_List[i][0]=Vijeth_List[i][0].split('.')

for i in range(len(Vijeth_List)):
    if Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'mp3' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'aac' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'flac':
        Vijeth_Music.append(Vijeth_List[i])
    elif Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'jpg' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'bmp' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'gif':
        Vijeth_Image.append(Vijeth_List[i])
    elif Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'mp4' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'avi' or Vijeth_List[i][0][len(Vijeth_List[i][0])-1] == 'mkv':
        Vijeth_Movie.append(Vijeth_List[i])
    else:
        Vijeth_Other.append(Vijeth_List[i])

# print(Vijeth_Music)
# print(Vijeth_Image)
# print(Vijeth_Movie)
# print(Vijeth_Other)

# for i in range(len(Vijeth_Music)):
#     Vijeth_Music[i][1]=Vijeth_Music[i][1].rstrip('b')
# # for i in range(len(Vijeth_Image)):
# #     Vijeth_Image[i][1]=Vijeth_Image[i][1].rstrip('b')
# for i in range(len(Vijeth_Movie)):
#     Vijeth_Movie[i][1]=Vijeth_Movie[i][1].rstrip('b')
# for i in range(len(Vijeth_Music)):
#     Vijeth_Other[i][1]=Vijeth_Other[i][1].rstrip('b')
# print(Vijeth_Music)
# print(Vijeth_Image)
# print(Vijeth_Movie)
# print(Vijeth_Other)

if not Vijeth_Music:
    Music_Size = 0
else:
    for i in range(len(Vijeth_Music)):
        Vijeth_Music[i][1]=Vijeth_Music[i][1].rstrip('b')
        Music_Size += int(Vijeth_Music[i][1])
if not Vijeth_Image:
    Image_Size_Size = 0
else:
    for i in range(len(Vijeth_Image)):
        Vijeth_Image[i][1]=Vijeth_Image[i][1].rstrip('b')
        Image_Size += int(Vijeth_Image[i][1])
if not Vijeth_Movie:
    Movie_Size_Size = 0
else:
    for i in range(len(Vijeth_Movie)):
        Vijeth_Movie[i][1]=Vijeth_Movie[i][1].rstrip('b')
        Movie_Size += int(Vijeth_Movie[i][1])
if not Vijeth_Other:
    Other_Size = 0
else:
    for i in range(len(Vijeth_Other)):
        Vijeth_Other[i][1]=Vijeth_Other[i][1].rstrip('b')
        Other_Size += int(Vijeth_Other[i][1])

Output = "Music" + ' ' + str(Music_Size) + 'b' + '\n' + "Images" + ' ' + str(Image_Size) + 'b' + '\n' + "Movies" + ' ' + str(Movie_Size) + 'b' + '\n' + "Other" + ' ' + str(Other_Size) + 'b'
print(Output)

