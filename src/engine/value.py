import math

class Value():
    """ stores a single scalar value and its gradient"""

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0

        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op # the op that produced this node, for graphviz

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other) # check that other is a Value object
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            

