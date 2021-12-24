from gauss_seidel import *

def omega_gauss_seidel(input_A, input_b, N, x0, tolerance_error,omega):
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

        G = ((D-omega*L).I)@((1-omega)*D+omega*U)
        f =  omega*((D-omega*L).I)@b
        for i in range(N):
            print(i, x_k, sep="\n")
            x_k_1 = G @ x_k + f
            if is_condition_enough(x_k, x_k_1, tolerance_error):
                return x_k_1
            else:
                x_k = x_k_1.copy()
        return "迭代失败,x{}\n{:s}".format(N,str(x_k))
    else:
        print("非严格对角占优，无法迭代")
    pass

if __name__ == '__main__':
    A_list = [[3.0,1.0],[1.0,2.0]]
    b_list = [[2.0,-1.0]]
    x0 = [[0, 0]]
    N = 25
    tolerance_error = 1e-4
    input_A = np.mat(A_list)
    input_b = np.transpose(np.array(b_list))  
    w = 1.25  
    print("超")
    print(omega_gauss_seidel(input_A, input_b, N, x0, tolerance_error,w), sep="\n")
