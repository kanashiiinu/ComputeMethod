from newton_interpolation import *
import sys
if __name__ == "__main__":
    inter_point_list = [[1.0, 1.0], [4.0, 2.0], [9.0, 3.0]]
    print("inter_point (x,y):")
    A_input = []
    for line in sys.stdin:
        if line=='\n': 
            break
        else:
            pass
        A_input.append(list(map(float,line.split())))
        pass
    print("input_num:")
    input_num = float(input())
    print("result is :")
    print(newton_interpolation(inter_point_list, input_num))
"""
x y
1 1
4 2
9 3

5
"""