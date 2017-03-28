'''
Created on Mar 28, 2017

@author: hongzhucui
'''
import powerset
import math

def lexical_transform(input_set):
    """
    a recursive function transform the 'out-of-order' input_set to the lexical-ordered powerset
    params:input_set: list[list[str]], 
    rtype: list[list[str]]
    """
    set_size = len(input_set)
    result_list = []
    if set_size == 1: return input_set 
    if set_size == 2: return input_set[-1:] + input_set[:-1]  # cyclic shift
    
    base_size = int(math.log(set_size, 2))
    start = 0
    for i in reversed(xrange(base_size)):
        tmp = lexical_transform(input_set[start:start+(1<<i)])
        result_list.extend(tmp)
        start += 1<<i
    result_list.append(input_set[start])
    return result_list[-1:]+result_list[:-1]  # cyclic shift

if __name__ == '__main__':
    test_set = [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
    print lexical_transform(test_set)
    