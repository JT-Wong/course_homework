# # -*- coding:utf-8 -*-
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
import random
# r=np.load('./data/有序数据/sum.npy')
# print(r)

# a = [['a', [1,1,1]], ['b', [2,2,2]], ['c', [3,3,3]]]
# random.shuffle(a)
# print(a)


# df = np.mat(np.array([[1,-1],[0,0],[1,-1]]))
# U,Sigma,VT = np.linalg.svd(df, full_matrices=True)
# print(U)
# print(Sigma)
# print(VT)
#
# print('.......')
# U,Sigma,VT = np.linalg.svd(df, full_matrices=False)
# print(U)
# print(Sigma)
# print(VT)

src_data = np.load('./result/random_projection/rp_gauss_res.npy')
print(src_data.shape)

# a = np.array([[1,2],[1,3],[1,4]])
# lsa = TruncatedSVD(1)
# res = lsa.fit_transform(a)
# print(res.shape)
# print(res)


# print(a)
# b = np.transpose(a)
# print(b)

# for i in range(100):
#     a = np.random.rand(1,1000)
#     b = np.random.rand(1,1000)
#     dis = np.linalg.norm(a - b)
#     print(dis)

# from sklearn.decomposition import TruncatedSVD
# X = np.load('./data/sum.npy')
# lsa = TruncatedSVD(500)
# X2 = lsa.fit_transform(X)
# print(X2.shape)
# np.save('./result/SVD/V_new.npy', X2)

# data = np.load('./result/random_projection/rp_gauss_res.npy')
# print(data.shape)
# f = open('./test.txt', 'w+')


# U = np.load('./result/SVD/U.npy')
# Sigma = np.load('./result/SVD/Sigma.npy')
# V = np.load('./result/SVD/V.npy')
# print(U.shape)
# print(Sigma.shape)
# print(V.shape)
# i = 500
# while i < len(Sigma):
#     Sigma[i] = 0
#     i += 1
#
# S = np.zeros((3040,3040))
# S[:3040,:3040] = np.diag(Sigma)
#
# t = np.dot(U, S)
# new_data = np.dot(t, V)
#
# np.save('./result/SVD/V_new.npy', new_data)

# data = np.load('./result/SVD/V_new.npy')
# for i in data[0]:
#     f.write(str(i) + '\n')
#
# print(data.shape)

#
# data = np.load('./result/SVD/V.npy')
# new_data = normalize(data, axis=0, norm='l2')
#
# np.save('./result/SVD/V_norm.npy', new_data)

# new_data = []
# for i in data:
#     t = []
#     for j in i:
#         if abs(j) < 0.001:
#             t.append(0.0)
#         else:
#             # print(j)
#             t.append(j)
#     new_data.append(t)
#
# data = np.asarray(new_data)
#
# np.save('./result/SVD/V_001.npy', data)

# data = np.load('./result/SVD/V_01.npy')

# for i in range(len(data)):
#     a = data[i]
#     j = i + 1
#     while j < len(data):
#         b = data[j]
#         c = a - b
#         dis = np.linalg.norm(c)
#         # dis = dis_count(c)
#         f.write(str(dis) + '\n')
#         j += 1
