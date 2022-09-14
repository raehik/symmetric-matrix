from smatrix import smatrix

def test_constructors():
  # All these constructors show succeed
  empty = smatrix.zeros([])
  singleton = smatrix.zeros([1])
  row = smatrix.zeros([1,2])