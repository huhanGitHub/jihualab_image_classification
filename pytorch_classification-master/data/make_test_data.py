test_data_path = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test'
test_result_path = 'D:\projects\pytorch_classification-master\pytorch_classification-master\data\\test_results.txt'

f = open(test_result_path, 'a+')
import os

#dirs = os.listdir(val_path)

for root, dirs, files, in os.walk(test_data_path, topdown=False):
    cla = root[root.rindex('\\')+1: len(root)]
    if cla != 'test':
        print('class:' + cla)
        for file in files:
            print('file:'+file)
            f.write(file[0:file.rindex('.')]+','+root[root.rindex('\\')+1: len(root)]+'\n')

f.close()

    # for dir in dirs:
    #     print('dir:'+dir)
