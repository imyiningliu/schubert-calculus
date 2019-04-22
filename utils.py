from schubert.gr import *
import numpy as np
import math
from itertools import combinations, permutations


def cutout(grass, young):
    r""" Returns cutout functions corresponding to schubert variety of grassmannian GRASS, indexed by YOUNG.

    Args:
    :grass: a Grassmannian object
    :young: a young_diagram object

    Examples:
        >>> grass = Gr(2, 4)
        >>> young = Young([1])
        >>> cutout(grass, young)
    """
    n = grass.n
    k = grass.k
    result = set()
    partition = young.partition
    dual_partition = [(grass.n - grass.k) - partition[i] for i in range(grass.k)][::-1]
    for tpl in combinations(range(n), k):
        flag = True
        for j in range(k):
            j = j + 1
            # print(dual_partition[k-j] + j + 1)
            if num_intersect(tpl, dual_partition[k-j] + j) < j:
                # print(tpl)
                flag = False
        if flag == False:
            result.add(tpl)
    return result


def num_intersect(tpl, m):
    count = 0
    for j in tpl:
        if j < m:
            count += 1
        else:
            break
    return count


def intersect_dual(grass, A, B, dual):
    partition = dual.partition
    dual_partition = [(grass.n - grass.k) - partition[i] for i in range(grass.k)][::-1]
    return intersection_cardinality(grass, A, B, Young(dual_partition))


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def intersection_cardinality(grass, A, B, C):
    r""" Returns dim of intersection.
        Args:
        :grass: the Grassmannian we're working with
        :A, B, C: Young diagrams
        """
    n = grass.n
    k = grass.k
    
    # all_equations = set(combinations(range(grass.n), grass.k))
    cutout_A = cutout(grass, A) # get cutout equations
    cutout_B = cutout(grass, B)
    cutout_C = cutout(grass, C)
    all_permutations = list(permutations(range(grass.n)))
    
    max_union_size = 0
    
    # get two permutations permute A and B
    pi_pairs = list(combinations(all_permutations, 2)) # combinations_with_replacement?
    for pi_1, pi_2 in pi_pairs:
        perm_cutout_A, perm_cutout_B = permute(pi_1, cutout_A), permute(pi_2, cutout_B)
        union_size = len(perm_cutout_A.union(perm_cutout_B, cutout_C))
        if union_size > max_union_size:
            max_union_size, max_permutations = union_size, [(pi_1, pi_2)]
        elif union_size == max_union_size:
            max_permutations.append([pi_1, pi_2])
    # print("Maximum number of cutout equations: %s" % (max_union_size))
    # return max_permutations
    return nCr(n,k) - max_union_size


def permute(pi, cutout_equations):
    r""" Permute indices of cutout equations according to pi.
        Args:
        :pi: a tuple representing a permutation.
        :cutout: a set of tuples indicating indices of cutout equations.
        """
    result = []
    for equation in cutout_equations:
        item = []
        for i in equation:
            item.append(pi[i])
        item.sort()
        result.append(tuple(item))
    return set(result)
