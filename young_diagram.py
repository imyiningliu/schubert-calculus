def non_increasing(L):
    return all(x>=y for x, y in zip(L, L[1:]))


class YoungDiagram(object):
    def __init__(self, partition):
        r""" A young diagram object.

        Args:
            :partition: a list of non-increasing integers.

        Example:
            >>> from young_diagram import *
            >>> young = Young([4, 3, 3])
            >>> young
        """
        assert non_increasing(partition)

        self.partition = partition
        self.diagram = []
        for i in partition:
            self.diagram.append([None] * i)

    def __repr__(self):
        string = ""
        for row in self.diagram:
            for char in row:
                if char is None:  # might need young tableau in the future?
                    string += "# "
                else:
                    string += str(char) + " "
            string += '\n'
        return string[:-1]
