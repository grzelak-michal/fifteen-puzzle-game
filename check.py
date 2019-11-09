class Assert(object):
    def __init__(self, actual):
        self.actual = actual
    
    def equals(self, expected):
        if expected != self.actual:
            self._raise(self.actual, expected)

    def _raise(self, actual, expected):
        raise AssertionError("Expected to be: {}, but actually is: {}".format(expected, actual))

def AssertTrue(actual):
    Assert(actual).equals(True)

def AssertFalse(actual):
    Assert(actual).equals(False)