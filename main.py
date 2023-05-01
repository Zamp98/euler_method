

y = 0.5
h=0.02
min = 0
max = 2
t=min


steps = int(max/h)
for a in range(0, steps):
    f = y - t * t + 1
    y = y + h*f
    t+=h
    print('%.4f' % (y), )