class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.end_of_list = False
        self.cache = None
        self.get_next_value()

    def peek(self):
        return self.cache

    def __next__(self):
        if self.end_of_list:
            raise StopIteration()
        cached_value = self.cache
        self.get_next_value()
        return cached_value

    def get_next_value(self):
        try:
            self.cache = self.iterator.__next__()
        except StopIteration:
            self.end_of_list = True

    def hasNext(self):
        return not self.end_of_list