import sys

import numpy as np

def is_list(x):
    """ x should be either list or int. """
    if isinstance(x, list):
        answer = True
    elif isinstance(x, int):
        answer = False
    else:
        sys.exit("input should be either list or int.")
    return answer

def int2list(x):
    if is_list(x) == False:
        x = [x]
    return x

def compare(x1, x2):
    global is_right_order
    while is_right_order == -1:
        for i, left in enumerate(x1):
            try: 
                right = x2[i]
            except IndexError:
                is_right_order = True
                break;
            print(f"{left} vs {right}")
            
            if is_list(left) == False and is_list(right) == False:
                if left < right:
                    is_right_order = True
                    break;
                elif left > right:
                    is_right_order = False
                    break;
            
            # elif is_list(left) == True and is_list(right) == True:
            #     x1 = left
            #     x2 = right
            #     compare(x1, x2)
                
            else:
                x1 = int2list(left)
                x2 = int2list(right)            
                #print(f">> {left} vs {right}")
                compare(x1, x2)
                
        return 


if __name__ == "__main__":
    #x1 = [[1],[2,3,4]]
    #x2 = [[1],4]
    x1 = [1]
    x2 = [1]
    is_right_order = -1
    compare(x1, x2)
    print(is_right_order)