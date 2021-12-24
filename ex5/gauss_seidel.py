import numpy.matlib
import numpy as np


def is_row_strictly_diagonally_dominant(input_A):
    n, m = input_A.shape
    A = np.array(input_A)
    for i in range(n):
        val_ii = abs(A[i][i])
        sum_other = 0
        for j in range(1, m):
            sum_other += abs(A[i][(i + j) % m])
        if val_ii > sum_other:
            pass
        else:
            return False
    return True


def get_lower_triangular_matrix(input_A):
    is_lower = lambda i, j: i > j
    L = get_index_element(input_A, is_lower)
    return L


def get_upper_triangular_matrix(input_A):
    is_upper = lambda i, j: i < j
    U = get_index_element(input_A, is_upper)
    return U


def get_pseudo_diagonal_matrix(input_A):
    is_diag = lambda i, j: i == j
    D = get_index_element(input_A, is_diag)
    return D


def get_index_element(input_A, is_condition_enough):
    A = np.array(input_A)
    n, m = A.shape
    A_arr = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if is_condition_enough(i, j):
                A_arr[i][j] = A[i][j]
            else:
                pass
    return np.mat(A_arr)


def gauss_seidel(input_A, input_b, N, x0, tolerance_error):
    """[summary]

    Args:
        input_A ([list]): [系数矩阵]
        input_b ([list]): []
        N ([int]): [最大迭代次数]
        x0 ([list]): [初始向量]
        tolerance_error ([float]): [误差限]
    """
    if is_row_strictly_diagonally_dominant(input_A):
        L = get_lower_triangular_matrix(input_A)
        D = get_pseudo_diagonal_matrix(input_A)
        U = get_upper_triangular_matrix(input_A)
        b = np.mat(input_b)
        n, m = np.array(x0).shape
        if n > m:
            x_k = np.mat(x0)
        else:
            x_k = np.mat(np.transpose(x0))

        intermediate_matrix = (D + L).I
        G = -intermediate_matrix @ U
        f = intermediate_matrix @ b

        for i in range(N):
            # print(i, x_k, sep="\n")
            x_k_1 = G @ x_k + f
            if is_condition_enough(x_k, x_k_1, tolerance_error):
                return x_k_1
            else:
                x_k = x_k_1.copy()
        return "迭代失败,x{}\n{:s}".format(N,str(x_k))
    else:
        print("非严格对角占优，无法迭代")
    pass


def is_condition_enough(x_k, x_k_1, tolerance_error):
    vec_err = np.abs(x_k_1 - x_k)
    for val in vec_err:
        if val > tolerance_error:
            return False
        else:
            pass
    return True


if __name__ == "__main__":

    N = 10 
    tolerance_error = 1e-5
    input_A = np.mat([[10, -1, -2], [-1, 10, -2], [-1, -1, 5]])
    input_b = np.transpose(np.mat([[7.2, 8.3, 4.2]]))
    x0 = [[0, 0, 0]]
    print(gauss_seidel(input_A, input_b, N, x0, tolerance_error), sep="\n")
