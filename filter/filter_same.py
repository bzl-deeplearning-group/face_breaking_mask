import hashlib
from glob import glob
import imagehash
from PIL import Image,ImageFile
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True
#去重
def hash_image():
    file_list = glob("../mask/mask/*.*")
    file_list = sorted(file_list)
    #print(file_list)
    hasharr = []
    for path in file_list:
        try:
            img = Image.open(path)
        except BaseException as e:
            os.remove(path)

        hash_1 = imagehash.average_hash(img)
        hasharr.append(hash_1)
    for index, each_hash in  enumerate( hasharr):
        try:
            val = hasharr.index(each_hash,index+1)
            os.remove(file_list[index])
        except ValueError as valError:
            pass
hash_image()