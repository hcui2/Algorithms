'''
Created on Mar 27, 2017

@author: hongzhucui
'''

def powerset_recursive(set):
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
        
if __name__ == '__main__':
    testset = ['a', 'b', 'c']
    all_subsets = powerset_recursive(testset)
    print all_subsets
    
    