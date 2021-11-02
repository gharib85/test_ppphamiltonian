
import numpy as np
from scipy.sparse import dok_matrix

u_matrix=np.arange(2)+1
v_matrix=(np.arange(4)+1).reshape((2,2))
k=u_matrix.shape[0]


two_electron_matrixu= dok_matrix((2*k, 2*k))
two_electron_matrixv= dok_matrix((2*k, 2*k))

for i in range(k):
    two_electron_matrixu[i,i+k] = u_matrix[i]
    two_electron_matrixu[i+k,i] = u_matrix[i]
for i in range(k):
    for j in range(i,k):
         v_ij = v_matrix[i, j]
         two_electron_matrixv[i, j] = v_ij
         two_electron_matrixv[j, i] = v_ij

         two_electron_matrixv[i, j+k] = v_ij
         two_electron_matrixv[j+k, i] = v_ij

         two_electron_matrixv[i+k, j] = v_ij
         two_electron_matrixv[j, i+k] = v_ij

         two_electron_matrixv[i+k, j+k] = v_ij
         two_electron_matrixv[j+k, i+k] = v_ij
two_electron_matrix=two_electron_matrixu+two_electron_matrixv
print("v+u")
print(two_electron_matrix.toarray())
print("_"*15)

# v_matrix over write u_matrix
#see  finalmatrix [2,2] is diffent




two_electron_matrix= dok_matrix((2*k, 2*k))


for i in range(k):
    two_electron_matrix[i,i+k] = u_matrix[i]
    two_electron_matrix[i+k,i] = u_matrix[i]
for i in range(k):
    for j in range(i,k):
         v_ij = v_matrix[i, j]
         two_electron_matrix[i, j] = v_ij
         two_electron_matrix[j, i] = v_ij

         two_electron_matrix[i, j+k] = v_ij
         two_electron_matrix[j+k, i] = v_ij

         two_electron_matrix[i+k, j] = v_ij
         two_electron_matrix[j, i+k] = v_ij

         two_electron_matrix[i+k, j+k] = v_ij
         two_electron_matrix[j+k, i+k] = v_ij

print("v over write u")
print(two_electron_matrix.toarray())
print("see position [2,2] for example")

