train_dataset_0 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\0'
train_dataset_1 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\1'
train_dataset_2 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\2'

import os
from PIL import Image

#category 0:  count*7 (45, 60, 90, 180, 270, LEFT_RIGHT, TOP_BOTTOM)
def process_category_0(path):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            im = Image.open(root+'/'+file)
            #print(file)
            im_rotate1 = im.rotate(45)
            im_rotate2 = im.rotate(60)
            im_rotate3 = im.transpose(Image.ROTATE_90)
            im_rotate4 = im.transpose(Image.ROTATE_180)
            im_rotate5 = im.transpose(Image.ROTATE_270)
            im_rotate6 = im.transpose(Image.FLIP_LEFT_RIGHT)
            im_rotate7 = im.transpose(Image.FLIP_TOP_BOTTOM)

            original_name = file[:file.rindex('.')]
            print(original_name)

            im_rotate1.save(root+'/'+original_name+'_1.png')
            im_rotate2.save(root + '/' + original_name + '_2.png')
            im_rotate3.save(root + '/' + original_name + '_3.png')
            im_rotate4.save(root + '/' + original_name + '_4.png')
            im_rotate5.save(root + '/' + original_name + '_5.png')
            im_rotate6.save(root + '/' + original_name + '_6.png')
            im_rotate7.save(root + '/' + original_name + '_7.png')

#category 1:  count*2 (LEFT_RIGHT)
def process_category_1(path):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            im = Image.open(root+'/'+file)
            im_rotate6 = im.transpose(Image.FLIP_LEFT_RIGHT)
            original_name = file[:file.rindex('.')]
            print(original_name)

            im_rotate6.save(root + '/' + original_name + '_6.png')

#category 2:  count*3 (LEFT_RIGHT, TOP_BOTTOM)
def process_category_2(path):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            im = Image.open(root+'/'+file)
            im_rotate6 = im.transpose(Image.FLIP_LEFT_RIGHT)
            im_rotate7 = im.transpose(Image.FLIP_TOP_BOTTOM)

            original_name = file[:file.rindex('.')]
            print(original_name)
            im_rotate6.save(root + '/' + original_name + '_6.png')
            im_rotate7.save(root + '/' + original_name + '_7.png')

if __name__ == '__main__':
    #process_category_0(train_dataset_0)
    process_category_1(train_dataset_1)
    process_category_2(train_dataset_2)