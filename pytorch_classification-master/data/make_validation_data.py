val_data_path = 'D:\\data\\data_processed\\val'
val_result_path = 'D:\\data\\data_processed\\val_results.txt'
f = open(val_result_path, 'a+')
import os

#dirs = os.listdir(val_path)

for root, dirs, files, in os.walk(val_data_path, topdown=False):
    print('root:'+root[root.rindex('\\')+1: len(root)])
    for file in files:
        print('file:'+file)
        f.write(file[0:file.rindex('.')]+','+root[root.rindex('\\')+1: len(root)]+'\n')

f.close()

    # for dir in dirs:
    #     print('dir:'+dir)
