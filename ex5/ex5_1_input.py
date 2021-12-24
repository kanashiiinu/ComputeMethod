from gauss_seidel import *

def input_matrix():
    import sys
    A_input = []
    for line in sys.stdin:
        if line=='\n': 
            break
        else:
            pass
        A_input.append(list(map(float,line.split())))
        pass
    try:
        A = np.mat(A_input)
    except Exception:
        raise Exception("is not a matrix")  
    return A
def is_square_matrix(A):
    if A.shape[0] != A.shape[1]:
        return False
    else:
        return True
    
def is_vector(b):
    if b.shape[0] != 1:
        return False
    else:
        return True
def is_match(A,b):
    if A.shape[0] == b.shape[1]:
        return True
    else:
        return False 

if __name__ == "__main__":
    while True:
        print("y or n")
        primitive_command = input()
        if primitive_command == "y":
            try:
                print("input A:")
                A_input = input_matrix()
                print(A_input)
                print("b:")
                b_input = input_matrix()      
                print(b_input)          
                if not is_match(A_input, b_input):
                    raise Exception("is not matched")
                else:
                    pass
                print("N:")
                N = int(input())
                print(N)
                print("x0:")
                x0 = input_matrix()
                if not is_match(A_input, x0):
                    raise Exception("is not matched")
                else:
                    pass
                print(x0)
                print("e:")
                e = float(input())
                print(e)
                print("result is :")
                try:
                    print(gauss_seidel(A_input, np.transpose(b_input), N, x0, e))
                except Exception:
                    print("error use")
                pass
            except Exception:
                print("error input")
            finally:
                continue
        elif primitive_command == "n":
            break
        else:
            print("error command")
            continue
"""
10 -1 -2
-1 10 -2
-1 -1 5

7.2 8.3 4.2

0 0 0
"""