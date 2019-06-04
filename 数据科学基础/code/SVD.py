# # -*- coding:utf-8 -*-
import numpy as np
import time
from sklearn.decomposition import TruncatedSVD

def svd_dim_redu(src_data_path, res_data_path, dim):
    src_data = np.load(src_data_path)
    src_data = np.transpose(src_data)
    print(src_data.shape)

    U, Sigma, V = np.linalg.svd(src_data, full_matrices=False)
    print(U.shape)
    print(Sigma.shape)
    print(V.shape)

    V = np.transpose(V)
    np.save(res_data_path, V)
    return



def truncated_svd_dim_redu(src_data_path, res_data_path, dim):
    src_data = np.load(src_data_path)

    lsa = TruncatedSVD(dim)
    res = lsa.fit_transform(src_data)

    np.save(res_data_path, res)
    return


b_t = time.time()
truncated_svd_dim_redu('./data/sum.npy', './result/SVD/tsvd_16.npy', 16)
e_t = time.time()
print(e_t-b_t)