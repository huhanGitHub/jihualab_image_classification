import os
path = 'D:\data\data_processed\png_data\\test\\3'
count = 81

for root, dirs, files in os.walk(path):
    print(root)
    for file in files:
        try:
            os.rename(root+'/'+file, root+'/'+str(count)+'.png')
            count += 1
        except Exception as e:
            print('exception:'+str(e))
