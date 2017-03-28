'''
Created on Mar 27, 2017

@author: hongzhucui
'''

def powerset_recursive(set):
    """
    a recursive implementation to generate the powerset
    params: set: list[str]
    rtype: list[list[str]]
    """
    result_list = powerset_helper(set, len(set))
    return result_list

def powerset_helper(set, index):
    all_subsets = [] 
    if index == 0:
        all_subsets.append([])
    else:
        all_subsets = powerset_helper(set, index -1 )
        more_subsets = []
        for subset in all_subsets:
            new_subset = subset[:] # list copy
            new_subset.append(set[index-1])
            more_subsets.append(new_subset)
        all_subsets.extend(more_subsets)

    return all_subsets;   

def powerset_combinatorics(set):
    result_list = []
    n = 1 << len(set) 
    for k in xrange(n):
        subset = convert(k,set)
        result_list.append(subset)
    return result_list

def convert(n, set):
    result_set  = []
    index = 0
    while (n > 0):
        if (n & 1) == 1: result_set.append(set[index])
        index += 1
        n = n >> 1
    return result_set

def powerset_combinatorics2(set):
    result_list = []
    n = 1 << len(set) 
    for k in xrange(n):
        subset = convert2(k,set)
        result_list.append(subset)
    return result_list

def convert2(n, set):
    result_set  = []
    index = 0
    while (n > 0):
        if (n & 1) == 0: result_set.insert(0,set[-index-1])
        index += 1
        n = n >> 1
    while (index < len(set)):
        result_set.insert(0, set[-index-1])
        index += 1
    return result_set
          
if __name__ == '__main__':
    testset = ['a', 'b', 'c']
    all_subsets = powerset_recursive(testset)
    all_subsets2 = powerset_combinatorics(testset)
    all_subsets3 = powerset_combinatorics2(testset)
    print all_subsets
    print all_subsets2
    print all_subsets3
    
    
    