import imageio.v3
filenames = ['1.png', '2.png']
images = []
for filename in filenames:
    images.append(imageio.v3.imread(filename))
imageio.v3.imwrite('some.gif', images, duration=500, loop=0)
