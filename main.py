import os, sys

print('==========================================')
print('REMOVE all photos with same name as movies')
print('==========================================')
print('Move this app to target directory or input full path under here, and press Enter to start.')
path = input('Path:')

if not path:
    path = './'
path = os.path.normpath(path)
print(path)

movie_extension = [".mp4", ".avi", ".rmvb", ".wmv", ".mov", ".mkv", ".flv", ".ts", ".webm", ".mpeg", ".mpg", ".vob"]

for folderName, folders, files in os.walk(path):
    for file in files:
        #filename = os.path.splitext(file)[0]
        #suffix = os.path.splitext(file)[1].replace('.', '')

        for suffix in movie_extension:
            if suffix in file:
                print('Found:', file)
                filename = os.path.splitext(file)[0]
                if os.path.exists(os.path.join(folderName, filename + '.jpg')):
                    os.remove(os.path.join(folderName, filename + '.jpg'))
                    print('Del:', filename + '.jpg')

        #if suffix in movie_extension:
                #    try:
                #        os.remove(os.path.join(folderName, filename + '.jpg'))
                #    print('Found:', file, 'deleted same name photo')
                #    except FileNotFoundError:
                #    print('Found:', file, 'skip')

print('Finished!')