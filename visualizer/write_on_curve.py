
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def draw_line(line_or,line_vecadd, marker, n_steps, step_size):  
    
    for i in range(n_steps):
        l = i*step_size
        x = line_or[0] + l*line_vecadd[0]
        y = line_or[1] +l*line_vecadd[1]
        ax.scatter(x, y, 0, marker=marker)


draw_line([2,2],[2,2], 'x', 20,0.05)
draw_line([4,2],[-2,2], 'o', 20,0.05)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()