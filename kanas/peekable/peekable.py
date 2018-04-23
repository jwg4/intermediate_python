class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = self.iterator.__next__()

    def peek(self):
        return self.cache

    def __next__(self):
        cached_value = self.cache
        self.cache = self.iterator.__next__()
        return cached_value

    def hasNext(self):
        pass