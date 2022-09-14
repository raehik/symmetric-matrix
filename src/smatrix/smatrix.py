def zeros(shape):
    """
    Return an symmetric matrix of given shape and type, filled with zeros.
    Parameters
    ----------
    shape : {sequence of ints}
        Shape of the matrix

    Returns
    -------
    out : matrix
        Zero matrix of given shape.
    """
    zeros_data = [[0 for _ in range(0, dim_size)] for dim_size in shape]
    smatrix(shape, zeros_data)
    
class smatrix:
    """
    Construct a symmetrix matrix
    Parameters
    ----------
    shape : {sequene of ints}
        Shape of the matrix

    data : {sequence of sequence of floats}
        Data for the symmetric matrix in row-order, where len(data[i]) = shape[i]
    """
    var_shape: list[int]
    var_data: list[float]
    def __init__(self, shape, data):
        # Check invariant
        for dim_size, row, dim in zip(shape, data, list(range(0,len(shape)))):
            if dim_size != len(row):
                raise DataException('Invalid data', 'Size of dimension ' + dim + ' does not match row length')
        # If we have reached here then the data invariant is met
        var_shape = shape
        var_data  = data

    #def toList(self):
        