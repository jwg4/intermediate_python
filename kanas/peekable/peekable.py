class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator

    def peek(self):
        pass

    def __next__(self):
        return self.iterator.__next__()

    def hasNext(self):
        pass