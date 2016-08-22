"""
def only_num_arguments(f):
    def new_f(a, b):
        if type(a) != int or type(b) != int:
            raise ValueError("Only int arguments!")
        return f(a, b)
    return new_f

"""

class only_num_arguments(object):
    def __init__(self, floats=True, ints=True):
        self.floats = floats
        self.ints = ints
    
    def __call__(self, f):
        def new_f(a, b):
            # checks
            return f(a, b)
        return new_f


@only_num_arguments(floats=True, ints=True)
def add(a, b):
    return (a + b)


print(add(2, 3))