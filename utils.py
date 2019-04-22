from schubert.gr import *
import numpy as np
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
    variety = grass.schubert_variety(young)
    zero_idx = np.argwhere(variety == 0)
    first_row_zeros = []
    for row, col in zero_idx:
        if row != 0:
            break
        first_row_zeros.append(col)
    result = set(combinations(first_row_zeros, grass.k))

    zero_col_idx = list(np.where(~variety.any(axis=0))[0])  # get all-zero columns in variety
    for idx in zero_col_idx:
        cols = list(range(grass.n))
        cols.remove(idx)
        new_results = set(combinations(cols, grass.k - 1))
        for new in new_results:
            result.add(list(new).append(idx))
    return result


def intersect_dual(grass, A, B, dual):
    partition = dual.partition
    dual_partition = [(grass.n - grass.k) - partition[i] for i in range(grass.k)][::-1]
    return intersection_cardinality(grass, A, B, Young(dual_partition))


def intersection_cardinality(grass, A, B, C):
    r""" Returns dim of intersection.
    Args:
        :grass: the Grassmannian we're working with
        :A, B, C: Young diagrams

    """
    # all_equations = set(combinations(range(grass.n), grass.k))
    cutout_A = cutout(grass, A) # get cutout equations
    cutout_B = cutout(grass, B)
    cutout_C = cutout(grass, C)
    all_permutations = list(permutations(range(grass.n)))

    max_union_size = 0

    # get two permutations permute A and B
    pi_pairs = list(combinations(all_permutations, 2))
    for pi_1, pi_2 in pi_pairs:
        perm_cutout_A, perm_cutout_B = permute(pi_1, cutout_A), permute(pi_2, cutout_B)
        union_size = len(perm_cutout_A.union(perm_cutout_B, cutout_C))
        if union_size > max_union_size:
            max_union_size, max_permutations = union_size, [(pi_1, pi_2)]
        elif union_size == max_union_size:
            max_permutations.append([pi_1, pi_2])
    print("Maximum number of cutout equations: %s" % (max_union_size))
    return max_permutations


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
