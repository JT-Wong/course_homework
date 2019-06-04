# # -*- coding:utf-8 -*-
import numpy as np
from PIL import Image
import os
import time
from skimage import io
import random




data = []
label_file = open('./data/faces94_label.csv', 'w+')
num = 0

src_dir_path = './data/faces94'
try:
    for s1 in os.listdir(src_dir_path):
        for s2 in os.listdir(src_dir_path + '/' + s1):

            for s3 in os.listdir(src_dir_path + '/' + s1 + '/' + s2):
                label = s1 + '_' + s2 + '_' + s3
                if len(s3.split('.')) != 3:
                    print(label)

                image = io.imread(src_dir_path + '/' + s1 + '/' + s2 + '/' + s3,as_gray=True)
                a1 = np.array(image)
                a2 = a1.flatten()

                num += 1
                if num % 100 == 0:
                    print(num)

                data.append([label, a2])

except :
    print(src_dir_path + '/' + s1 + '/' + s2 + '/' + s3)

# 打乱数据
random.shuffle(data)

sum_array = []

for d in data:
    label = d[0]
    arr = d[1]
    sum_array.append(arr)
    label_file.write(label + '\n')

np.array(sum_array)
np.save('./data/sum.npy', sum_array)

label_file.close()









