import os

def createIfNotExists(folder):
    if(not os.path.exists(folder)):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

files=os.listdir()
files.remove("Auto_Folder_Clean.py")
print(files)

#os.makedirs("Images")    Agar file already bana hua h toh, Error throw karega..
# if (not os.path.exists('Images')):
#     os.makedirs('Images')

createIfNotExists('Images')
createIfNotExists('Doc')
createIfNotExists('Media')
createIfNotExists('Other')

ImgExt=[".jpg",".jpeg",".png"]
Images=[file for file in files if os.path.splitext(file)[1].lower() in ImgExt]

docExt=['.docx','.doc','.pdf','.txt']
Doc=[file for file in files if os.path.splitext(file)[1].lower() in docExt]

mediaExt=['.mp4','.mp3','.mkv']
Medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

Others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if(ext not in ImgExt) and (ext not in docExt) and (ext not in mediaExt) and(os.path.isfile(file)):
        Others.append(file)

# for media in Medias:
#     os.replace(media,f"Media/{media}")
move("Images",Images)
move("Doc",Doc)
move("Media",Medias)
move("Other",Others)
