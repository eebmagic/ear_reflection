import matplotlib.pyplot as plt
from random import randint

def rand_point(low, high):
    x = randint(low, high)
    y = randint(low, high)
    z = randint(low, high)

    point = (x, y, z)
    return point


def avg_point(pointlist):
    '''
    returns the point at the center of the given pointlist
    '''
    X = [p[0] for p in pointlist]
    Y = [p[1] for p in pointlist]
    Z = [p[2] for p in pointlist]

    x = sum(X) / len(pointlist)
    y = sum(Y) / len(pointlist)
    z = sum(Z) / len(pointlist)

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


def reflect_point(point, plane):
    '''
    returns the point in the reflection of the plane
    '''
    x1, y1, z1 = point
    a, b, c, d = plane

    # find point on plane perp to point
    k =(-a * x1-b * y1-c * z1-d)/float((a * a + b * b + c * c)) 
    x2 = a * k + x1
    y2 = b * k + y1
    z2 = c * k + z1
    
    # find point equidistant from plane as original
    x3 = 2 * x2-x1
    y3 = 2 * y2-y1
    z3 = 2 * z2-z1

    mid = (x2, y2, z2)
    reflected = (x3, y3, z3)
    return reflected, mid


# Make three random points
MIN, MAX = 0, 100
a = rand_point(MIN, MAX)
b = rand_point(MIN, MAX)
c = rand_point(MIN, MAX)
print(a, b, c)
center_point = avg_point([a, b, c])
print(center_point)

# Make a plane from those three points
plane = make_plane(a, b, c)
print(f"Plane: {plane[0]}x + {plane[1]}y + {plane[2]}z + {plane[3]} = 0")

# Make random point off axis
point_off_plane = rand_point(MIN, MAX)

# Get the reflection of the off point
reflected_point, mid_point = reflect_point(point_off_plane, plane)


# Chart data
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# chart points
ax.plot(*zip(point_off_plane, mid_point, reflected_point), color='b', linestyle='-', marker='o')

# plot to center point
ax.plot(*zip(point_off_plane, center_point, reflected_point), color='r', marker='o')

# chart plane
ax.plot_trisurf(*zip(a, b, c))
plt.show()