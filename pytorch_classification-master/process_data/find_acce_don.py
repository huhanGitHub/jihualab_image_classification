tadf_path = 'D:\data\data_processed\data with DA\\train\\2'
prefix = 'EM-TADF-'

donor_path = 'D:\data\machie learning data\Donor\png'
acceptor_path = 'D:\data\machie learning data\Acceptor\png'

final_output = 'D:\data\data_processed\data with DA\\train\\2_DA'

import os
import shutil

tadf_pics = []
for root, dirs, files in os.walk(tadf_path):
    for file in files:
        if file.startswith(prefix):
            tadf_pics.append(root+'\\'+file)
            str = final_output+'\\'+file.split('.')[0]
            if not os.path.isdir(str):
                os.makedirs(str)
            else:
                print('dir '+str +' exists')
            shutil.copy(root + '\\' + file, str + '\\' + file)

# copy all donors to the same directory as TADF
for root, dirs, files in os.walk(donor_path):
    for donor in files:
        donor_name = donor.split('.')[0]
        donor_number = donor_name.split('-')[2]
        #print('donor file:' + donor)
        #print('donor number:' + donor_number)
        for tadf in tadf_pics:
            tadf_name = tadf.split('.')[0]
            tadf_number = tadf_name.split('-')[2]
            if tadf_number.strip() == donor_number.strip():
                file = tadf_name.split('\\')[-1]
                print('tadf number:'+tadf_number)
                print('donor number:' + donor_number)
                output = final_output+'\\'+file
                if os.path.isdir(output):
                    shutil.copy(root+'\\'+donor, output+'\\'+donor.replace(' ', ''))

# copy all acceptors to the same directory as TADF
for root, dirs, files in os.walk(acceptor_path):
    for acceptor in files:
        acceptor_name = acceptor.split('.')[0]
        acceptor_number = acceptor_name.split('-')[2]
        print('acceptor file:' + acceptor)
        print('acceptor number:' + acceptor_number)
        for tadf in tadf_pics:
            tadf_name = tadf.split('.')[0]
            tadf_number = tadf_name.split('-')[2]
            if tadf_number.strip() == acceptor_number.strip():
                file = tadf_name.split('\\')[-1]
                print('tadf number:'+tadf_number)
                print('acceptor number:' + acceptor_number)
                output = final_output+'\\'+file
                if os.path.isdir(output):
                    shutil.copy(root+'\\'+acceptor, output+'\\'+acceptor.replace(' ', ''))


