from young_diagram import *
import numpy as np


class Gr(object):
    r""" A Gr(k, n) object, representing the set of dim k subspace of n dim
    vector space.

    Args:
        :k: dim of subspace
        :n: dim of vector space

    Examples:
        >>> from grassmannian import *
        >>> grass = Gr(2, 4)

    """
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.size = (k, n)

    def schubert_cell(self, young):
        r""" Create a schubert cell.

        Args:
            :young: a Young diagram object used to index schubert cells

        Examples:
            >>> young = YoungDiagram([2, 1])
            >>> grass = Gr(2, 4)
            >>> grass.schubert_cell(young)
        """
        def generate_cell(k, n, partition):
            schubert_cell = np.full((k, n), -1) # -1 refers to star

            if partition == []:  # empty young diagram
                schubert_cell[:, n-k:] = np.identity(k)
                return schubert_cell

            if k == 1:  # one-dim subspaces
                one_idx = n - partition[0] - 1
                schubert_cell[0][one_idx] = 1
                schubert_cell[0][one_idx + 1:] = 0
                return schubert_cell

            if partition[0] == n - k:  # recursive case
                schubert_cell[0, :] = 0
                schubert_cell[:, 0] = 0
                schubert_cell[0, 0] = 1
                schubert_cell[1:, 1:] = generate_cell(k-1, n-1, partition[1:])
            else:
                schubert_cell[:, 1:] = generate_cell(k, n-1, partition)

            return schubert_cell

        return generate_cell(self.k, self.n, young.partition)