import os
import shutil
import sys
from time import sleep
from tkinter import filedialog, Tk

def choose_directory():
    directory_root = Tk()
    directory_root.withdraw()
    path_work = filedialog.askdirectory()
    if path_work == '':
        print('Wrong path, choose again please.')
        sleep(2)
        return choose_directory()
    else:
        # askdirectory 获得是 正斜杠 路径C:/，所以下面要把 / 换成 反斜杠\
        return path_work.replace('/', os.sep)


print('============================================')
print('COPY&RENAME all photos in Extras and Gallery')
print('============================================')
path = choose_directory()

#path = os.path.normpath(path)
print(path)
print('==========================================')
print('1. Extras')
print('2. Gallery')
print('3. Extras & Gallery')
got_input = input('Choose processing range: ')
if got_input == "1":
    extras_mark = True
    gallery_mark = False
elif got_input == "2":
    extras_mark = False
    gallery_mark = True
elif got_input == "3":
    extras_mark = True
    gallery_mark = True
else:
    print('Wrong range')
    sys.exit(1)
print('==========================================')
movie_extension = [".mp4", ".avi", ".rmvb", ".wmv", ".mov", ".mkv", ".flv", ".ts", ".webm", ".mpeg", ".mpg", ".vob"]
pic_extension = [".jpg", ".png", ".jpeg"]

for folderName, folders, files in os.walk(path):
    # print(folders, files)
    # 搜索所有符合条件的根目录
    for folder in folders:
        if (extras_mark and folder == 'Extras') or (gallery_mark and (folder == 'Gallery' or 'Gallery' in folderName)):
            print('Loading:', os.path.join(folderName, folder))
            # 列出子目录文件
            proc_dir = os.path.join(folderName, folder)
            for filename in os.listdir(proc_dir):
                file_path = os.path.join(proc_dir, filename)
                try:
                    # 跳过文件夹
                    if os.path.isdir(file_path):
                        continue

                    # 跳过非图片
                    if not (filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg")):
                        continue

                    dest_path = os.path.join(proc_dir, os.path.splitext(filename)[0] + '.mov')
                    if not os.path.exists(dest_path):
                        shutil.copyfile(file_path, dest_path)
                        print('Copy & Rename:', file_path, dest_path)
                    else:
                        print('Existed:', dest_path)
                except Exception as e:
                    print('Error:', file_path, e)
            print('==========================================')
print('Done!')
if sys.platform == 'win32':
    os.system("pause")
"""    
    for file in files:
        #filename = os.path.splitext(file)[0]
        #suffix = os.path.splitext(file)[1].replace('.', '')
        for suffix in movie_extension:
            if suffix in file:
                filename = os.path.splitext(file)[0]
                if os.path.exists(os.path.join(folderName, filename + '.jpg')):
                    print('Found:', file, 'and', filename + '.jpg, ', end='')
                    #os.remove(os.path.join(folderName, filename + '.jpg'))
                    print('Del:', filename + '.jpg')
                else:
                    print('Found:', file)

        #if suffix in movie_extension:
                #    try:
                #        os.remove(os.path.join(folderName, filename + '.jpg'))
                #    print('Found:', file, 'deleted same name photo')
                #    except FileNotFoundError:
                #    print('Found:', file, 'skip')
"""
