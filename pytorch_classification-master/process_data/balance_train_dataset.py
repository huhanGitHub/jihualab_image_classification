train_dataset_0 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\0'
train_dataset_1 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\1'
train_dataset_2 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\2'
train_dataset_3 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\train\\3'

val_dataset_0 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\val\\0'
val_dataset_1 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\val\\1'
val_dataset_2 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\val\\2'
val_dataset_3 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\val\\3'

test_dataset_0 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test\\0'
test_dataset_1 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test\\1'
test_dataset_2 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test\\2'
test_dataset_3 = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test\\3'

import os
from PIL import Image

#category 0:  count*9 (45, 60, 90, 180, 270, LEFT_RIGHT, TOP_BOTTOM, 300, 330), 60*10
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
            im_rotate8 = im.rotate(300)
            im_rotate9 = im.rotate(330)
            original_name = file[:file.rindex('.')]
            print(original_name)

            im_rotate1.save(root+'/'+original_name+'_1.png')
            im_rotate2.save(root + '/' + original_name + '_2.png')
            im_rotate3.save(root + '/' + original_name + '_3.png')
            im_rotate4.save(root + '/' + original_name + '_4.png')
            im_rotate5.save(root + '/' + original_name + '_5.png')
            im_rotate6.save(root + '/' + original_name + '_6.png')
            im_rotate7.save(root + '/' + original_name + '_7.png')
            im_rotate8.save(root + '/' + original_name + '_8.png')
            im_rotate9.save(root + '/' + original_name + '_9.png')

#category 1:  count*2 (LEFT_RIGHT), 263*2
def process_category_1(path):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            im = Image.open(root+'/'+file)
            im_rotate6 = im.transpose(Image.FLIP_LEFT_RIGHT)
            original_name = file[:file.rindex('.')]
            print(original_name)

            im_rotate6.save(root + '/' + original_name + '_6.png')

#category 2:  count*3 (LEFT_RIGHT, TOP_BOTTOM), 183*3
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

#category 3:  count*9 (45, 60, 90, 180, 270, LEFT_RIGHT, TOP_BOTTOM, 300, 330), 61*10
def process_category_3(path):
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
            im_rotate8 = im.rotate(300)
            im_rotate9 = im.rotate(330)
            original_name = file[:file.rindex('.')]
            print(original_name)

            im_rotate1.save(root+'/'+original_name+'_1.png')
            im_rotate2.save(root + '/' + original_name + '_2.png')
            im_rotate3.save(root + '/' + original_name + '_3.png')
            im_rotate4.save(root + '/' + original_name + '_4.png')
            im_rotate5.save(root + '/' + original_name + '_5.png')
            im_rotate6.save(root + '/' + original_name + '_6.png')
            im_rotate7.save(root + '/' + original_name + '_7.png')
            im_rotate8.save(root + '/' + original_name + '_8.png')
            im_rotate9.save(root + '/' + original_name + '_9.png')

if __name__ == '__main__':
    process_category_0(train_dataset_0)
    process_category_1(train_dataset_1)
    process_category_2(train_dataset_2)
    process_category_3(train_dataset_3)

    process_category_0(val_dataset_0)
    process_category_1(val_dataset_1)
    process_category_2(val_dataset_2)
    process_category_3(val_dataset_3)

    process_category_0(test_dataset_0)
    process_category_1(test_dataset_1)
    process_category_2(test_dataset_2)
    process_category_3(test_dataset_3)