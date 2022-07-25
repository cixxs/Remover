import os, sys

# 切换工作目录
config_path = '/'.join((sys.argv[0].replace('\\', '/')).split('/')[:-1])
work_path = os.getcwd().replace('\\', '/')
if work_path != config_path:
    os.chdir(config_path)

print('==========================================')
print('REMOVE all photos with same name as movies')
print('==========================================')
print('Move this app to target directory or input full path under here, and press Enter to start.')
path = input('Path:')

if not path:
    path = './'
else:
    path = path.replace('\\', '')

print(path)

movie_extension = ["mp4", "avi", "rmvb", "wmv", "mov", "mkv", "flv", "ts", "webm", "mpeg", "mpg", "vob"]

for folderName, folders, files in os.walk(path):
    for file in files:
        filename = os.path.splitext(file)[0]
        suffix = os.path.splitext(file)[1].replace('.', '')
        if suffix in movie_extension:
            try:
                os.remove(os.path.join(folderName, filename + '.jpg'))
                print('Found:', file, 'deleted same name photo')
            except FileNotFoundError:
                print('Found:', file, 'skip')

print('Finished!')