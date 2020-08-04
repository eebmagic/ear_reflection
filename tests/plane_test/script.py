import matplotlib.pyplot as plt
from random import randint

def rand_point(low, high):
    x = randint(low, high)
    y = randint(low, high)
    z = randint(low, high)

    point = (x, y, z)
    return point


def make_plane(a, b, c):
    '''
    make a plane from three points
        a, b, c - a point as a tuple (x, y, z)
        return: the values in a formula eqation for the plane
            (a, b, c, d)
        where:
            ax + by + cz + d = 0
    '''
    x1, y1, z1 = a
    x2, y2, z2 = b
    x3, y3, z3 = c
    
    # ab
    a1 = x2 - x1 
    b1 = y2 - y1 
    c1 = z2 - z1 
    # ac
    a2 = x3 - x1 
    b2 = y3 - y1 
    c2 = z3 - z1 
    
    # ab x ac
    a = b1 * c2 - b2 * c1 
    b = a2 * c1 - a1 * c2 
    c = a1 * b2 - b1 * a2 
    d = (- a * x1 - b * y1 - c * z1)

    return (a, b, c, d)


# Make three random points
MIN, MAX = 0, 100
a = rand_point(MIN, MAX)
b = rand_point(MIN, MAX)
c = rand_point(MIN, MAX)
print(a, b, c)

# Make a plane from those three points
plane = make_plane(a, b, c)
print(f"Plane: {plane[0]}x + {plane[1]}y + {plane[2]}z + {plane[3]} = 0")

# Make random points on that plane
x_rand = []
y_rand = []
z_rand = []
total = 30
for _ in range(total):
    x = randint(MIN, MAX)
    y = randint(MIN, MAX)
    # z = -(ax + by + d)
    z = (-((plane[0]*x) + (plane[1]*y) + plane[3])) / plane[2]

    # new_point = (x, y, z)
    # random_points.append(new_point)
    x_rand.append(x)
    y_rand.append(y)
    z_rand.append(z)

# Chart data
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(*zip(a, b, c), color='r', marker='o')
ax.plot(x_rand, y_rand, z_rand, color='b', linestyle='-', marker='o', markersize=1)
plt.show()