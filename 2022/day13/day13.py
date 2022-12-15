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

def compare(x1, x2, debug=False):
    global is_right_order
    while is_right_order == -1:
        for i, left in enumerate(x1):
            #print(i)
            try: 
                right = x2[i]
            except IndexError:
                is_right_order = False
                if debug:
                    print(f"len({x1}) > len({x2})")
                sys.exit();
            
            if is_list(left) == False and is_list(right) == False:
                if left < right:
                    is_right_order = True
                    if debug:
                        print(f"{left} < {right}")
                    break;
                elif left > right:
                    is_right_order = False
                    if debug:
                        print(f"{left} > {right}")
                    break;
                
            else:
                if debug:
                        print(f">> {left} vs {right}")
                compare(int2list(left), int2list(right), debug=debug)
                if is_right_order == True or is_right_order == False:
                    break;                    
                    
        if is_right_order==-1 and len(x1)<len(x2):
            is_right_order = True
            if debug:
                print(f"len({x1}) < len({x2})")
            break;
        return 

if __name__ == "__main__":
    x1 = [[1],[2,3,4]]
    x2 = [[1],4]
    is_right_order = -1
    compare(x1, x2, debug=True)
    print(is_right_order)