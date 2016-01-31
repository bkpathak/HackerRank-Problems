"""
The problem definition is here:
http://codereview.stackexchange.com/questions/38500/rainfall-challenge

The implementaion here uses union-find data structures.
"""


class Basin(object):
    """
    This class tracks the sink for each basin and number of cells that belongs
    to the basin.
    """
    def __init__(self,map_size):
        self.basin = [-1] * map_size
        # representative member of the Basin(set)
        self.sink = None
        self.count = 0

    def add_cell_to_basin():
        """
        This is the union operation in the UNION-FIND data struccture.
        """


class Cell(object):
    """
    Keep tracks of to which basin the cell belongs to.
    """
    def __init__(self):
        self.to_basin = None

    def find_basin():
        """
        This is find operation of UNION-FIND data structure.
        """

class Topography(object):
    """
    Run through the elevation data and find to which basins each cells belongs to.
    """

def find_basin(elevation):
    """
    Find the number of basin in the data.
    """
    for
