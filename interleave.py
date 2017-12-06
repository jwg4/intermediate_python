class Queue(object):
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data = [value] + self.data

    def get(self):
        value = self.data[-1]
        self.data = self.data[:-1]
        return value

    def __str__(self):
        strings = [ str(i) for i in self.data ]
        l_str = ", ".join(strings)
        return ">> [ %s ] >>" % (l_str, )


class Stack(object):
    def __init__(self, data=[]):
        self.data = data

    def push(self, value):
        self.data = [value] + self.data

    def pop(self):
        if not len(self.data):
            return None
        value = self.data[0]
        self.data = self.data[1:]
        return value

    def __str__(self):
        strings = [ str(i) for i in self.data ]
        l_str = ", ".join(strings)
        return "(TOP) %s ]" % (l_str, )


def interleave(queue, stack):
    end = False
    count = 0
    while not end:
        v = stack.pop()
        if v is None:
            end = True
        else:
            count = count + 1
            queue.add(v)
    print "FILLED Q", stack, queue

    n = (count + 1) / 2

    for i in range(0, n):
        v = queue.get()
        stack.push(v)
    print "HALF-FILLED S", stack, queue

    if count * 2 != n:
        x = stack.pop()
        queue.add(x)
        n = n - 1
    print "MOVED ODD ELEMENT", stack, queue

    for i in range(0, n):
        print "ABOUT TO MOVE", stack, queue
        v = queue.get()
        queue.add(v)
        print "MOVED Q ELEMENT", stack, queue
        v = stack.pop()
        queue.add(v)
        print "MOVED S ELEMENT", stack, queue
    print "DONE LOOP", stack, queue

    for i in range(0, count):
        v = queue.get()
        stack.push(v)
    print "TRANSFERRED TO STACK", stack, queue


def get_interleaved(input_data):
    q = Queue()
    s = Stack(input_data)
    interleave(q, s)
    output_data = s.data
    return output_data


if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7]
    print input_data
    output_data = get_interleaved(input_data)
    print output_data
         
