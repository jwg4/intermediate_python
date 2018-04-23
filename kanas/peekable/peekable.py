class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.get_next_value()

    def peek(self):
        return self.cache

    def __next__(self):
        cached_value = self.cache
        self.get_next_value()
        return cached_value

    def get_next_value(self):
        self.cache = self.iterator.__next__()

    def hasNext(self):
        pass