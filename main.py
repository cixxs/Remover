import os
import shutil

print('============================================')
print('COPY&RENAME all photos in Extras and Gallery')
print('============================================')
print('Move this app to target directory or input full path under here, and press Enter to start.')
path = input('Path:')

if not path:
    path = './'

path = os.path.normpath(path)
print(path)
print('==========================================')
movie_extension = [".mp4", ".avi", ".rmvb", ".wmv", ".mov", ".mkv", ".flv", ".ts", ".webm", ".mpeg", ".mpg", ".vob"]
pic_extension = [".jpg", ".png", ".jpeg"]

for folderName, folders, files in os.walk(path):
    # print(folders, files)
    # 搜索所有符合条件的根目录
    for folder in folders:
        if folder == 'Extras' or folder == 'Gallery' or 'Gallery' in folderName:
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
