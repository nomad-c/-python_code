import os
import shutil

path = "E:\\czarny\\Desktop\\360pictures\\"
file_dir = os.listdir(path)

try:
    os.mkdir(path + "downloaded_images")
except:
    print("Folder already found")
for file in file_dir:
    print(file)
    split_tup = os.path.splitext(file)
    file_extension = split_tup[1]
    print(file_extension)
    if (
        (file_extension == ".jpeg")
        or (file_extension == ".png")
        or (file_extension == ".jpg")
    ):
        old_path = path + file
        new_path = path + "downloaded_images\\" + file
        shutil.move(old_path, new_path)
    else:
        pass
