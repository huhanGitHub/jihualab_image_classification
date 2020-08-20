import os
from PIL import Image

width_i = 480
height_i = 480

data_dir = r"D:\data\data_processed\data with DA\train\2_DA"
#final_name = dir_name+'\merge'

def concat_images(dir_name):
    print(dir_name)
    all_path = list()
    final_name = dir_name + '\merge'
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            # check D and A
            if file.startswith('TADF-D') or file.startswith('TADF-A'):
                # collect all pic paths
                all_path.append(os.path.join(root, file))

    if len(all_path) < 2:
        print('all path is {}, less than 2. Pls check {}'.format(len(all_path), dir_name))
        return

    # 1. A + B --> AB
    toImage1 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage1.paste(pic1, (0, 0))
    toImage1.paste(pic2, (1*width_i, 0))

    #toImage1.show()
    toImage1.save(final_name+'_1.png')

    # 2. A + B --> BA
    toImage2 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic1, (1*width_i, 0))
    toImage2.paste(pic2, (0, 0))

    #toImage2.show()
    toImage2.save(final_name+'_2.png')

    # 3. A + B --> A/B
    toImage2 = Image.new('RGBA', (height_i * 1, width_i * 2))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic1, (0, 1*width_i))
    toImage2.paste(pic2, (0, 0))

    #toImage2.show()
    toImage2.save(final_name+'_3.png')

    # 4. A + B --> B/A
    toImage2 = Image.new('RGBA', (height_i * 1, width_i * 2))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic1, (0, 0))
    toImage2.paste(pic2, (0, 1*width_i))

    #toImage2.show()
    toImage2.save(final_name+'_4.png')

    # 5. A + B --> A (flip left right) B
    toImage2 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))
    pic1 = pic1.transpose(Image.FLIP_LEFT_RIGHT)

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic1, (0, 0))
    toImage2.paste(pic2, (1*width_i, 0))

    #toImage2.show()
    toImage2.save(final_name+'_5.png')

    # 6. A + B --> A (flip top bottom) B
    toImage2 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))
    pic1 = pic1.transpose(Image.FLIP_TOP_BOTTOM)

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic1, (0, 0))
    toImage2.paste(pic2, (1*width_i, 0))

    #toImage2.show()
    toImage2.save(final_name+'_6.png')

    # 7. A + B --> A B(flip left right)
    toImage2 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))
    pic2 = pic2.transpose(Image.FLIP_LEFT_RIGHT)

    toImage2.paste(pic1, (0, 0))
    toImage2.paste(pic2, (1*width_i, 0))

    #toImage2.show()
    toImage2.save(final_name+'_7.png')

    # 8. A + B --> A B(flip top bottom)
    toImage2 = Image.new('RGBA', (height_i * 2, width_i * 1))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))
    pic2 = pic2.transpose(Image.FLIP_TOP_BOTTOM)

    toImage2.paste(pic1, (0, 0))
    toImage2.paste(pic2, (1*width_i, 0))

    #toImage2.show()
    toImage2.save(final_name+'_8.png')

    # 9. A + B --> B/A（flip left right）
    toImage2 = Image.new('RGBA', (height_i * 1, width_i * 2))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))
    pic1 = pic1.transpose(Image.FLIP_LEFT_RIGHT)

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))

    toImage2.paste(pic2, (0, 0))
    toImage2.paste(pic1, (0, 1*width_i))

    #toImage2.show()
    toImage2.save(final_name+'_9.png')

    # 10. A + B --> A/B(flip top bottom)
    toImage2 = Image.new('RGBA', (height_i * 1, width_i * 2))
    #print(len(all_path))
    pic1 = Image.open(all_path[0])
    pic1 = pic1.resize((width_i, height_i))

    pic2 = Image.open(all_path[1])
    pic2 = pic2.resize((width_i, height_i))
    pic2 = pic2.transpose(Image.FLIP_TOP_BOTTOM)

    toImage2.paste(pic2, (0, 1*width_i))
    toImage2.paste(pic1, (0, 0))

    #toImage2.show()
    toImage2.save(final_name+'_10.png')

if __name__ == '__main__':
    print('begin')
    for root, dirs, files in os.walk(data_dir):
        for dir in dirs:
            concat_images(root+'\\'+dir)