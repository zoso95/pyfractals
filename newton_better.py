import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

coef = np.random.normal(size=6)*np.random.binomial(n=1, p=0.5, size=6)

def f(z):
    return coef[0]+coef[1]*z+coef[2]*z*z+coef[3]*z*z*z+coef[4]*z*z*z*z+coef[5]*z*z*z*z*z

def df(z):
    return coef[1]+2*coef[2]*z+3*coef[3]*z*z+4*coef[4]*z*z*z+5*coef[5]*z*z*z*z


def render(imgsize):
    y, x = np.ogrid[1: -1: imgsize*2j, -1: 1: imgsize*2j]
    z = x +y*1j

    img = np.zeros(z.shape)
    for i in tqdm(range(200)):
        #print("Iteration ", i)
        z = z - f(z)/df(z)
        ind = np.logical_and(np.abs(f(z)) < 1e-4, img==0)
        img[ind] = i

    fig = plt.figure(figsize=(imgsize/100.0, imgsize/100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis('off')

    cmaps = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool',
            'hot', 'afmhot', 'gist_heat', 'copper', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']

    c = np.random.choice(cmaps)
    ax.imshow(img, cmap=c)
    print(c)
    #ax.imshow(img, cmap="gist_gray")
    fig.savefig('output/high/newton-{}-{}.png'.format(coef, c))

if __name__ == '__main__':
    render(imgsize=1000)
