import scipy.sparse as sp
import numpy as np
from numpy.linalg import norm
from scipy.spatial import distance
arr = np.array(
    [[1,2],
    [2,1]
    ]
)


mat2 = sp.csr_matrix(arr).getrow(0).toarray()
n = np.array([0,0,0])
p = {1:12,2:11,3:111,4:0}
print(type(sorted(p.items(),key = lambda x:x[1])))