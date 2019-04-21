from schubert.gr import *
import numpy as np
from itertools import combinations


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
            result.add(new + (idx,))
    return result


def max_cut_off(A, B, C):
    r"""

    :param A: list of
    :param B:
    :param C:
    :return:
    """


