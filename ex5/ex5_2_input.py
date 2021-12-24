from gauss_elimination_method import *
from ex5_1_input import *
if __name__ == '__main__':
    A = input_matrix()
    A_list = A
    if is_non_singular_matrix(A_list):
        print(gauss_elimination_compute_determinant(A_list))
    else:
        print("error")
        pass
    pass
"""
3 -2 1 4
-7 5 -3 -6
2 1 -1 3
4 -3 2 8
"""