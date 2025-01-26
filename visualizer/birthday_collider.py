import random

from matplotlib import pyplot as plt
import numpy as np
num_people = 20
num_iter = 100000

#simulate birthday collisions over n people

def run(num_people, num_iter):
    days = []

    for i in range(365):
        days.append(i + 1)
    num_collision = 0

    for i in range(num_iter):
        collider = set({})
        for y in range(num_people):
            day = random.choice(days)
            if (day in collider):
                num_collision = num_collision + 1
            collider.add(day)      
    print("num_collision " + str(num_collision) + " num_iter " + str(num_iter))
    return num_collision


num_collision = run(num_people, num_iter)

y = np.array([num_iter, num_collision])
mylabels = ["Number of Experiments", "Number of collisions over " +str(num_people) + " people" ]


plt.pie(y, labels = mylabels)
plt.show() 

