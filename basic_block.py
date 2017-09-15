class BasicBlock(object):
    def __init__(self, block_size):
        self.size = block_size

    def top_number(self, n):
        return (n / self.size + 1) * self.size

    def block_contains(self, n):
        return (n / self.size + 1)
