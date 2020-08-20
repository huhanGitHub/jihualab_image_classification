import shutil
import os

origin_path = 'D:\data\data_processed\data with DA\\train\\2_DA'
destination_path = 'D:\data\data_processed\data with DA\\train\\2_all\\'

for root, dirs, files in os.walk(origin_path):
    print(root)
    for dir in dirs:
        print(dir)
        for root2, dirs2, files2 in os.walk(root+'\\'+dir):
            for file in files2:
                print(file)
                destination = destination_path
                if file.startswith('EM-TADF') or file.startswith('merge'):
                    if file.startswith('merge'):
                        destination = destination + dir+'_'
                    print(destination+file)
                    shutil.copy(root2+'\\'+file, destination+file)

