'''
Created on Mar 27, 2017

@author: hongzhucui
'''


def powerset(set):
    """
    :type set: List[str]
    :rtype: List[List[str]]
    """
    result_list = powerset_helper(set, 0)
    return result_list

def powerset_helper(set, index):
    """
    :type list:List[str]
    :type index:int
    :rtype: List[List[str]]
    """
    all_subsets = [] 
    if len(set) == index:
        all_subsets.append([])
    else:
        all_subsets = powerset_helper(set, index+1)
        more_subsets = []
        for subset in all_subsets:
            # list copy
            new_subset = subset[:]
            new_subset.append(set[index])
            more_subsets.append(new_subset)
        all_subsets.extend(more_subsets)
    return all_subsets;
        
        
if __name__ == '__main__':
    testset = ['a', 'b', 'c']
    all_subsets = powerset(testset)
    print all_subsets
    
    