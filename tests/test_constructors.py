from smatrix import smatrix

def test_constructors():
  # All these constructors show succeed
  empty = smatrix.zeros(0)
  assert empty.data == []

  singleton = smatrix.zeros(1)
  assert singleton.data == [[0]]
  
  two = smatrix.zeros(2)
  assert two.data == [[0, 0], [0]]