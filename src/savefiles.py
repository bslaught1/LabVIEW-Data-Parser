import os
import csv
from scipy.io import savemat
from openpyxl import Workbook

# saves data sets to csv file
def save_to_csv(data, file_path):
    # create new path
    path, _ = os.path.splitext(file_path)
    new_path = path + '.csv'
    
    var_order = 'xyzabcdefghijklmnopqrstuvw'    # order in which variables will be named

    # create rows filled with dicts
    rows = []
    for set_num, dset in enumerate(data):       # loop though data sets
        for row in range(dset.shape[0]):        # loop through rows
            if len(rows) <= row:
                rows.append(dict())             # if the row doesn't exist yet, make a new one
            for col in range(dset.shape[1]):
                rows[row][f'Set{set_num+1} {var_order[col]}'] = dset[row,col]   #set dict values for each variable

    # create file with dict writer
    with open(new_path, 'w', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        csv_writer.writeheader()
        for row in rows:
            csv_writer.writerow(row)
    
    return new_path


def save_to_xl(data, file_path):
    # create new_path
    path, _ = os.path.splitext(file_path)
    new_path = path + '.xlsx'

    wb = Workbook()

    sheets = []
    for idx in range(len(data)):
        if idx == 0:
            sheets.append(wb.active)
            sheets[0].title = f'Set {idx+1}'
        else:
            sheets.append(wb.create_sheet(title=f'Set {idx+1}'))
    
    for idx, dset in enumerate(data):
        for row in range(dset.shape[0]):
            vals = []
            for col in range(dset.shape[1]):
                vals.append(dset[row,col])
            sheets[idx].append(vals)

    wb.save(filename=new_path)

    return new_path


def save_to_mat(data, file_path):
    # create new_path
    path, _ = os.path.splitext(file_path)
    new_path = path + '.mat'
    
    # create matlab dictionary
    mat_dic = dict()
    for count, dset in enumerate(data):
        mat_dic[f'set{count+1}'] = dset
    
    # save file (thanks for doing all the work scipy :)
    savemat(new_path, mat_dic)
    return new_path


# creates test data for me to test each function
def test_data(num=6):
    import numpy as np
    x = [1, 2, 3, 4, 5]
    y = [1, 5, 3, 2, 4]

    data = []
    for _ in range(num):
        data.append(np.array([x, y]).transpose())
    return data
