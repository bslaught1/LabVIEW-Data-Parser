import numpy as np

# takes a list of strings and converts values to floats
def list_strToFloat(val_list):
    for idx, strg in enumerate(val_list):
        val_list[idx] = float(strg)
    return val_list


# function for collecting data
def colect_data(lines, start_idx):
    datapoints = []
    for line_num in range(start_idx, len(lines)):
        if lines[line_num] != '':
            values = list_strToFloat(lines[line_num].split('\t'))
            datapoints.append(values)
        else:
            break
    array = np.array(datapoints)

    # return array.transpose(), line_num    # Not sure if i should transpose or not
    return array, line_num


# Parses thorugh .lvm files and returns list of np.arrays
def parse_lvm(filename):
    with open(filename, 'r') as f:
        file_text = f.read()
    lines = file_text.splitlines()
    
    data_list = []
    line_num = 0
    while line_num < len(lines):
        if lines[line_num] == '***End_of_Header***\t\t':
            data, last = colect_data(lines, line_num+2)
            data_list.append(data)
            line_num = last

        line_num += 1

    return data_list


# Takes data list from parse_lvm and turns it into data information text
def data_to_infotxt(data):
    info_text = 'Data information:\n\n'
    set_num = len(data)
    info_text += f'Number of Data Sets: {set_num}\n\n'
    for count, array in enumerate(data):
        size = array.shape
        info_text += f'Set: {count+1}\tSize: {size[0]} x {size[1]}\n'
    return info_text
