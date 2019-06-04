# -*- coding:utf-8 -*-
import numpy as np


# 计算两个向量之间的距离
def cal_2_elem(a, b):
    dis = np.linalg.norm(a - b)
    return dis

# 计算某个向量属于哪一类
def cal_class(x, class_dict):
    min_dis = -1
    res = 'none'

    for c in class_dict:
        y = class_dict[c]
        dis = cal_2_elem(x, y)

        if min_dis == -1:
            min_dis = dis
            res = c
        elif dis < min_dis:
            min_dis = dis
            res = c

    return res

# 提取降维后数据里每一类的参考数据
def extra_control_data(label_file_path, data_file_path, res_label_file_path, res_data_file_path):

    dic = {}

    data = np.load(data_file_path)

    label_file = open(label_file_path)
    lines = label_file.readlines()
    for i in range(len(lines)):
        if lines[i].strip().split('.')[1] == '1':
            dic[lines[i].strip().split('.')[0]] = data[i]

    d = []
    res_label_f = open(res_label_file_path, 'w+')
    for l in dic:
        d.append(dic[l])
        res_label_f.write(l + '\n')
    res_label_f.close()

    np.array(d)
    np.save(res_data_file_path, d)

    return

# 对数据进行分类
def predict(data_file_path, standard_label_file_path, standard_data_file_path, res_file_path):
    data = np.load(data_file_path)

    standard_dict = {}
    standard_data = np.load(standard_data_file_path)
    standard_label_file = open(standard_label_file_path)
    lines = standard_label_file.readlines()
    for i in range(len(lines)):
        standard_dict[lines[i].strip()] = standard_data[i]

    i = 0
    res_file = open(res_file_path, 'w+')
    for x in data:
        predict_label = cal_class(x=x, class_dict=standard_dict)
        res_file.write(predict_label + '\n')
        i += 1

        if i == 24:
            print(i)


        if i % 100 == 0:
            print(i)
    res_file.close()

    return

# 结果评估
def res_assessment(label_file_path, predict_file_path):
    label_file = open(label_file_path)
    predict_file = open(predict_file_path)

    sum_num = 0
    right_num = 0
    wrong_num = 0


    label_lines = label_file.readlines()
    predict_lines = predict_file.readlines()
    for i in range(len(label_lines)):
        label = label_lines[i].strip()
        predict = predict_lines[i].strip()
        if predict in label:
            right_num += 1
        else:
            wrong_num += 1

    right_num -= 152
    sum_num = right_num + wrong_num


    print(right_num)
    print(wrong_num)
    print(right_num/sum_num)

    return



# extra_control_data('./data/faces94_label.csv', './result/SVD/V.npy', './result/SVD/standard_label.csv', './result/SVD/standard_img.npy')
# predict('./result/SVD/V.npy', './result/SVD/standard_label.csv', './result/SVD/standard_img.npy', './result/SVD/predict_label.csv')
# res_assessment('./data/faces94_label.csv', './result/SVD/predict_label.csv')

extra_control_data('./data/faces94_label.csv', './result/SVD/tsvd_16.npy', './result/SVD/standard_label.csv','./result/SVD/standard_img.npy')
predict('./result/SVD/tsvd_16.npy', './result/SVD/standard_label.csv', './result/SVD/standard_img.npy','./result/SVD/predict_label.csv')
res_assessment('./data/faces94_label.csv', './result/SVD/predict_label.csv')





# extra_control_data('./data/faces94_label.csv', './result/random_projection/rp_gauss_res.npy', './result/random_projection/guass_standard_label.csv', './result/random_projection/guass_standard_img.npy')
# predict('./result/random_projection/rp_gauss_res.npy', './result/random_projection/guass_standard_label.csv', './result/random_projection/guass_standard_img.npy', './result/random_projection/guass_predict_label.csv')
# res_assessment('./data/faces94_label.csv', './result/random_projection/guass_predict_label.csv')
#
#
# extra_control_data('./data/faces94_label.csv', './result/random_projection/rp_sparse_res.npy', './result/random_projection/sparse_standard_label.csv', './result/random_projection/sparse_standard_img.npy')
# predict('./result/random_projection/rp_sparse_res.npy', './result/random_projection/sparse_standard_label.csv', './result/random_projection/sparse_standard_img.npy', './result/random_projection/sparse_predict_label.csv')
# res_assessment('./data/faces94_label.csv', './result/random_projection/sparse_predict_label.csv')



# extra_control_data('./data/faces94_label.csv', './result/original/sum.npy', './result/original/standard_label.csv', './result/original/standard_img.npy')
# predict('./result/original/sum.npy', './result/original/standard_label.csv', './result/original/standard_img.npy', './result/original/predict_label.csv')
# res_assessment('./data/faces94_label.csv', './result/original/predict_label.csv')


# extra_control_data('./data/faces94_label.csv', './result/pca/pca_152.npy', './result/pca/standard_label.csv', './result/pca/standard_img.npy')
# predict('./result/pca/pca_152.npy', './result/pca/standard_label.csv', './result/pca/standard_img.npy', './result/pca/predict_label.csv')
# res_assessment('./data/faces94_label.csv', './result/pca/predict_label.csv')