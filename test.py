import scipy.sparse as sp
import numpy as np
from numpy.linalg import norm
from scipy.spatial import distance
arr = np.array([[0, 0, 0],
                [8, 0, 0],
                [0, 5, 4],
                [0, 0, 0],
                [0, 0, 7]])


mat2 = sp.csr_matrix(arr).getrow(0).toarray()
n = np.array([0,0,0])
print(mat2[0])
# # print(mat2)
# d = np.diff(mat2.indptr)
# # print(mat2.multiply(d).todense())
# print(mat2.multiply([1,2,3]).todense())
# # print(np.log10(10/d))

def cos_sim(array1,array2):
    cos = np.dot(array1,array2)/(norm(array1)*norm(array2))
    return cos

n1 = np.array([1,0,0])
# n2 = np.array([1,1,0])
# print(cos_sim(n1,mat2))