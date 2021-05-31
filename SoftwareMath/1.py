import numpy as np

a = np.array([[1,6],[5,2]])

eig = np.linalg.eig(a)


print("eigenvalues =", eig[0])

print("eigenvectors")
print(eig[1])