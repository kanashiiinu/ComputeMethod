# 2019215049汪海涛
from numpy.core.fromnumeric import shape
import numpy.matlib
import numpy as np


#this is a function that use gauss elimination to compute the val of determinant
def is_non_singular_matrix(A_input):
    A = np.array(A_input)
    is_n_eq_m = A.shape[0] == A.shape[1]
    is_n_eq_rank = np.linalg.matrix_rank(A) == A.shape[0]
    return is_n_eq_m and is_n_eq_rank


def gauss_elimination_compute_determinant(A_input: list):
    A = np.array(A_input)
    exchange_total = 0
    for i in range(A.shape[0]):
        A_sector, exchange_num = get_column_primary_element(A[i:, i:])
        exchange_total += exchange_num
        row_k = A_sector[0][:]
        for j in range(1, A_sector.shape[0]):
            A_sector[j] = A_sector[j] - row_k * A_sector[j][0] / row_k[0]
        A_sector[0] = row_k
    res = 1.0
    for i in range(A.shape[0]):
        res *= A[i][i]
    if exchange_total % 2 == 1:
        res = 0 - res
    else:
        pass
    return res


def get_column_primary_element(A_input):
    A = A_input
    max_raw_index = np.argmax(A[:][0], axis=0)
    if max_raw_index == 0:
        return A, 0
    else:
        for i in range(A.shape[0]):
            old_row = np.copy(A[0][:])
            A[0][:] = A[max_raw_index][:]
            A[max_raw_index][:] = old_row
            pass
        return A, 1


if __name__ == "__main__":
    A_list = [[3.0, -2.0, 1.0, 4.0], [-7.0, 5.0, -3.0, -6.0],
              [2.0, 1.0, -1.0, 3.0], [4.0, -3.0, 2.0, 8.0]]

    if is_non_singular_matrix(A_list):
        print(gauss_elimination_compute_determinant(A_list))
    else:
        pass
