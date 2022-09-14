from smatrix import smatrix

def test_constructors():
  # All these constructors show succeed
  empty = smatrix.zeros(0)
  singleton = smatrix.zeros(1)
  two = smatrix.zeros(2)