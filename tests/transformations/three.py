import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt


def center_of_mass(verts):
    x, y, z = 0, 0, 0
    for v in verts:
        x += v[0]
        y += v[1]
        z += v[2]
    x = x / len(verts)
    y = y / len(verts)
    z = z / len(verts)

    return (x, y, z)


def xy_angle(point):
    '''
    returns the angle of the point from the positive x-axis
    '''
    m = point[1] / point[0]
    theta = math.degrees(math.atan(m))
    if point[0] < 0:
        theta += 180

    return math.radians(theta)


def xz_angle(point):
    m = point[2] / point[0]
    theta = math.degrees(math.atan(m))
    if point[0] < 0:
        theta += 180

    return math.radians(theta)


def xy_rotation(vert, angle):
    c, s = math.cos(angle), math.sin(angle)
    matr = np.array(((c, s, 0), (-s, c, 0), (0, 0, 1)))
    v = np.array(vert)
    
    out = np.matmul(matr, v)
    out = out.tolist()
    return out


def xy_rotate_all(verts, angle):
    out = []
    for vert in verts:
        out.append(tuple(xy_rotation(vert, angle)))

    return out


def xz_rotation(vert, angle):
    c, s = math.cos(angle), math.sin(angle)
    matr = np.array(((c, 0, s), (-s, 0, c), (0, 1, 0)))
    v = np.array(vert)

    out = np.matmul(matr, v)
    out = out.tolist()
    return out


def xz_rotate_all(verts, angle):
    out = []
    for vert in verts:
        new = xz_rotation(vert, angle)
        out.append(new)

    return out


if __name__ == "__main__":
    from mpl_toolkits.mplot3d import Axes3D
    count = 10
    MAX, MIN = 70, 100
    points = []
    for i in range(count):
        x, y, z = randint(MAX, MIN), randint(MAX, MIN), randint(MAX, MIN)
        point = (x, y, z)
        points.append(point)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for x, y, z in points:
        ax.scatter(x, y, z, marker='o', color='blue')

    ax.scatter(0, 0, 0, marker='o', color='orange')
    ax.scatter(*zip(center_of_mass(points)), color='red')

    # xy rotation
    center = center_of_mass(points)
    angle = xy_angle(center)
    points = xy_rotate_all(points, angle)
    for x, y, z in points:
        ax.scatter(x, y, z, marker='o', color='blue')
    ax.scatter(*zip(center_of_mass(points)), color='orange')

    # xz rotation
    center = center_of_mass(points)
    angle = xz_angle(center)
    points = xz_rotate_all(points, angle)
    for x, y, z in points:
        ax.scatter(x, y, z, marker='o', color='blue')
    ax.scatter(*zip(center_of_mass(points)), color='yellow')
    print(center)
    print(center_of_mass(points))

    plt.show()