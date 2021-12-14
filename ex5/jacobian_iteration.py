from gauss_seidel import*

def jacobian_iteration(input_A, input_b, N, x0, tolerance_error):
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
        # 迭代方程系数的计算不同
        G = -D.I @ (L+U)
        f = D.I @ b
        # 迭代计算结果
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

if __name__== "__main__":
            
    N = 30
    tolerance_error = 1e-8
    input_A = np.mat([[3,1], [1,2]])
    input_b = np.transpose(np.array([[2,1]]))
    x0 = [[0, 0]]
    print(jacobian_iteration(input_A, input_b, N, x0, tolerance_error), sep="\n")
        