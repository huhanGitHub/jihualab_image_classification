# -*- coding: utf-8 -*-
import xlrd
import shutil

base_path = 'D:\\data\\machie learning data\\TADF-All\\'
copy_base_path = 'D:\\data\\data_processed\\train\\'

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\projects\jihualab\data\processed-data.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())
    # #获取sheet2
    # sheet1= workbook.sheet_names()[0]
    # print sheet2_name
    # # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_name('Sheet1')
    # # sheet的名称，行数，列数
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    for i in range(1, sheet1.nrows):
        try:
            light_len = int(sheet1.cell(i, 7).value)
            file = sheet1.cell(i, 13).value.strip()
            tif_path = base_path + file + '.tif'
            if light_len >= 580:
                copy_path = copy_base_path + '0//' + file + '.tif'
                path = shutil.copy(tif_path, copy_path)
                #print(path)
            if 580 > light_len >= 490:
                copy_path = copy_base_path + '1//' + file + '.tif'
                path = shutil.copy(tif_path, copy_path)
                #print(path)
            if light_len < 490:
                copy_path = copy_base_path + '2//' + file + '.tif'
                path = shutil.copy(tif_path, copy_path)
                #print(path)
        except FileNotFoundError:
            print('no file:'+file)
        except ValueError:
            print('value error')

if __name__ == '__main__':
    read_excel()