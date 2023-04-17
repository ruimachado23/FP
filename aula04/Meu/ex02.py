print("{:2s} {:2s} {:2s}".format("n", "n²", "2^n"))
a = range(1,21)
for n in a:
    print("{:2d} {:2d} {:2d}".format(n, n**2, 2**n))