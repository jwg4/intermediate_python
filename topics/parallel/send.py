def print_me(count):
    i = 0
    while i < count:
        val = (yield i)
        if val is not None:
            i = val
        else:
            i += 1

gen = print_me(10)

for i in gen:
   if i == 5:
       gen.send(8)
   else:
       print i

# https://stackoverflow.com/questions/20579756/passing-value-to-yield-using-send
# 0, 1, 2, 3, 4, 9