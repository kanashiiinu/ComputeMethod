from numpy.core.fromnumeric import shape
import numpy.matlib
import numpy as np
    
#this is a function that use gauss elimination to compute the val of determinant
def is_non_singular_matrix(A_input):
    A = np.array(A_input)
    is_n_eq_m = A.shape[0] == A.shape[1]  
    is_n_eq_rank = np.linalg.matrix_rank(A) == A.shape[0] 
    return is_n_eq_m and is_n_eq_rank

def gauss_elimination_compute_determinant(A_input:list):
    A = np.array(A_input)
    for i in range(A.shape[0]):
        A_sector = A[i:,i:]
        row_k = A_sector[0][:]
        for j in range(1,A_sector.shape[0]):
            A_sector[j] = A_sector[j] - row_k * A_sector[j][0] / row_k[0]
        A_sector[0] = row_k
    res = 1.0
    for i in range(A.shape[0]):
        res *= A[i][i]
    return res


if __name__ == "__main__":
    A_list = [[3.0, -2.0, 1.0, 4.0], 
              [-7.0, 5.0, -3.0, -6.0], 
              [2.0, 1.0, -1.0, 3.0], 
              [4.0, -3.0, 2.0, 8.0]]

    if is_non_singular_matrix(A_list):
        print(gauss_elimination_compute_determinant(A_list))
    else:
        pass
