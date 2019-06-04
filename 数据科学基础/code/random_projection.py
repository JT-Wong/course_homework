# # -*- coding:utf-8 -*-
import numpy as np
from sklearn import random_projection
import time

def svd_dim_redu(src_data_path, res_data_path):
    src_data = np.load(src_data_path)
    # src_data = src_data[:100]
    print(src_data.shape)

    transformer = random_projection.GaussianRandomProjection()
    # transformer = random_projection.SparseRandomProjection()
    res = transformer.fit_transform(src_data)
    print(res.shape)

    np.save(res_data_path, res)
    return



b_t = time.time()
# svd_dim_redu('./data/sum.npy', './result/random_projection/rp_gauss_res.npy')
# svd_dim_redu('./data/sum.npy', './result/random_projection/test.npy')
e_t = time.time()
print(e_t-b_t)


# b_t = time.time()
# svd_dim_redu('./data/sum.npy', './result/random_projection/rp_sparse_res.npy')
# e_t = time.time()
# print(e_t-b_t)