from manimlib.imports import *
import matplotlib.pyplot as plt

## mmandelbrot set
# the code below mainly refers to cigar666
# https://www.bilibili.com/video/av80245693

iter_func=lambda z,c: (z**2+c)

def calc_steps(c,max_iter_num=128):
    z=complex(0,0)
    num=0
    while abs(z)<2 and num<max_iter_num:
        z=iter_func(z,c)
        num+=1
    return num

def display_mandelbrot(x_num=1000,y_num=1000):
    X,Y=np.meshgrid(np.linspace(-8,8,x_num+1),np.linspace(-4,4,y_num+1))
    C=X+Y*1j
    result=np.zeros((y_num+1,x_num+1))

    for i in range(y_num+1):
        for j in range(x_num+1):
            result[i,j]=calc_steps(C[i,j])

    plt.imshow(result,interpolation='bilinear',cmap=plt.cm.hot,
                vmax=abs(result).max(),vmin=abs(result).min(),
                extent=[-8,8,-4.5,4.5])
    plt.show()

if __name__=='__main__':
    # set_gpus([0,1])
    display_mandelbrot(16000,8000)
