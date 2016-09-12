import os
import numpy as np


def get_data(filename):

    filepath = os.getcwd() + "\\" + filename + ".txt"
    file_array = open(filepath)


    raw_lines = [x[:-1].split(" ") for x in file_array.readlines()]
    capacity = int(raw_lines[0][0])
    values_and_sizes = np.array([(int(x),int(y)) for x, y in raw_lines[1:]])

    file_array.close()

    return capacity, values_and_sizes[:,0], values_and_sizes[:,1]

