from matplotlib import pyplot as plt

def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    return n

y_list=[]
x_list = []
for i in range(32):
    y_list.append(fib(i))
    x_list.append(i)

plt.scatter(x_list,y_list, color='red')
plt.show() 