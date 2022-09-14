import typing

def zeros(shape: int):
    """
    Return an symmetric matrix of given shape and type, filled with zeros.
    Parameters
    ----------
    shape : int
        Shape of the matrix

    Returns
    -------
    out : SMatrix
        Zero matrix of given shape.
    """
    row_sizes = reversed(range(1, shape + 1))
    zeros_data = [[0.0 for _ in range(0, row_size)] for row_size in row_sizes]
    return Smatrix(shape, zeros_data)
    
class Smatrix:
    # Attributes
    shape: int        = 0
    data: list[float] = []

    """
    Construct a symmetrix matrix (necessarily a square matrix)
    Parameters
    ----------
    shape : int
        Size of the matrix

    data : {sequence of sequence of floats}
        Data for the symmetric matrix in row-order, where len(data[i]) = shape[i]
    """
    def __init__(self, shape: int, data: list[float]):
        # Check invariants on relationship between shape and data
        for row, size in zip(data, reversed(range(1, shape + 1))):
            if len(row) != size:
                raise RuntimeError('Invalid data', 'Row of length ' + str(len(row)) + ' should be of length ' + str(size))
        # If we have reached here then the data invariant is met
        self.shape = shape
        self.data  = data

    """
    Outputs a list representation of the full matrix
    
    Returns
    -------
    out : {sequence of sequences of floats}
    """
    # def to_list(self):
    #     return self.var_data # for row in var_data
