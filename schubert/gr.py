from schubert.young import *
import numpy as np


class Gr(object):
    r""" A Gr(k, n) object, representing the set of dim k subspace of n dim
    vector space.

    Args:
        :k: dim of subspace
        :n: dim of vector space

    Examples:
        >>> from schubert.gr import *
        >>> grass = Gr(2, 4)

    """
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.size = (k, n)

    def __repr__(self):
        return 'Gr(%s, %s)' % (self.k, self.n)

    def schubert_cell(self, young):
        r""" Returns a schubert cell indexed by YOUNG diagram. "-1" refers to "star".

        Args:
            :young: a YoungDiagram object used to index schubert cells

        Examples:
            >>> from schubert.gr import *
            >>> young = Young([2, 1])
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

    def schubert_variety(self, young):
        r""" Returns a schubert variety indexed by YOUNG diagram. "-1" refers to "star".

        Args:
            :young: a YoungDiagram object used to index schubert varieties.

        Examples:
            >>> from schubert.gr import *
            >>> young = Young([2, 1])
            >>> grass = Gr(2, 4)
            >>> grass.schubert_variety(young)
        """
        cell = self.schubert_cell(young)
        one_idx = np.argwhere(cell == 1)
        for row, col in one_idx:
            cell[row, :col + 1] = -1
        return cell


