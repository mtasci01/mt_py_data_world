from matplotlib import pyplot as plt

def harmonic_series():
    N_ITER = 1000000
    STEP_SIZE = 10000
    xs=[]
    ys=[]
    sum = 0
    for i in range(1,N_ITER):
        if (i % STEP_SIZE == 0): 
            xs.append(i)
            ys.append(sum)
        sum = sum + 1/i

    plt.scatter(xs,ys, color='red')
    plt.show()   

harmonic_series()      