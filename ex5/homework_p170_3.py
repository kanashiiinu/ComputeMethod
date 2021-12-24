from jacobian_iteration import *
from gauss_seidel import *

if __name__ == '__main__':
    A_list = [[10.0, -1.0, 2.0, 0.0], 
              [-1.0, 11.0, -1.0, 3.0],
              [2.0, -1.0, 10.0, -1.0],
              [0.0, 3.0, -1.0, 8.0]]
    b_list = [[6.0, 25.0, -11.0, 15.0]]
    x0 = [[0, 0, 0, 0]]
    N = 25
    tolerance_error = 1e-3
    input_A = np.mat(A_list)
    input_b = np.transpose(np.array(b_list))    
    print("雅")
    print(jacobian_iteration(input_A, input_b, N, x0, tolerance_error),sep="\n")
    print("高")
    print(gauss_seidel(input_A, input_b, N, x0, tolerance_error), sep="\n")
    
