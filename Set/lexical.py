'''
Created on Mar 28, 2017

@author: hongzhucui
'''
import powerset
import math
from Set.powerset import powerset_combinatorics2
from aetools import test

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

def nth_subset(set, k):
    """ given the original set and index k, we compute the k+1 in lexical ordered powerset. 
        params: set list[str]
        params: k int
        rtype: list[str]
    """ 
    result =  []
    for bit_index in reversed(range(1, len(set)+1)):
        if ((k >> bit_index) & 1)==0:
            ones = (1<< bit_index) -1
            if (k & ones): k -= 1
            else: k |= ones
    
    start = 0
    for bit_index in xrange(len(set)):    
        real_index = len(set)- 1 - bit_index
        if (k& (1 << real_index)) == 0:
            result.append(set[start])
        start += 1
    return result
        
        
    
if __name__ == '__main__':
    test_set = [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
    print lexical_transform(test_set)
    # test2 = powerset_combinatorics2(['a','b','c','d'])
    # print lexical_transform(test2)
    test_set2 = ['a', 'b', 'c', 'd']
    for i in range(16):
        result = nth_subset(test_set2, i)
        print result
    