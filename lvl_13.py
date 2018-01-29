data = open("evil2.gfx", "rb").read()
for i in range(5):
    open('%d_evil.jpg' % i ,'wb').write(data[i::5])
