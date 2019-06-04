# # -*- coding:utf-8 -*-
import numpy as np
import time
from sklearn.decomposition import PCA

def svd_dim_redu(src_data_path, res_data_path, dim):
    src_data = np.load(src_data_path)
    # data = np.zeros((9120,36000))
    # data[:3040] = src_data
    # data[3040:6080] = src_data
    # data[6080:] = src_data
    # print(data.shape)


    lsa = PCA(n_components=dim, svd_solver='auto')
    res = lsa.fit_transform(src_data)

    print(res.shape)
    res = res[:3040]
    np.save(res_data_path, res)
    return


b_t = time.time()
svd_dim_redu('./data/sum.npy', './result/pca/pca_152.npy', 152)
e_t = time.time()
print(e_t-b_t)