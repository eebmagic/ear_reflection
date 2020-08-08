import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt

def get_angle(point):
    m = point[1] / point[0]
    theta = math.degrees(math.atan(m))
    if point[0] < 0:
        theta += 180

    return math.radians(theta)


def center_of_mass(points):
    x, y = 0, 0
    for point in points:
        x += point[0]
        y += point[1]

    x /= len(points)
    y /= len(points)

    center = (x, y)
    return center


def rotation(point, angle):
    '''
    rotates right by angle
    where angle is in radians?
    '''
    c, s = math.cos(angle), math.sin(angle)
    matr = np.array(((c, s), (-s, c)))
    v = np.array((point[0], point[1]))

    out = np.matmul(matr, v)
    out = out.tolist()
    return out


def rotate_all(points, angle):
    out = []
    for point in points:
        out.append(rotation(point, angle))

    return out


if __name__ == "__main__":
    size = 10
    X = [randint(30, 60) for i in range(size)]
    Y = [randint(30, 60) for i in range(size)]
    points = [(X[i], Y[i]) for i in range(size)]
    original_center = center_of_mass(points, )

    # Rotate all points to readjust center of mass
    new_points = rotate_all(points, get_angle(original_center))
    new_center = center_of_mass(new_points)

    print(f"old angle: {get_angle(original_center)}")
    print(f"new angle: {get_angle(new_center)}")

    for i in range(size):
        point = (X[i], Y[i])
        angle = get_angle(point)
        print(point, angle, math.degrees(angle))

        plt.plot(*zip(point, (0,0)))
        plt.plot(*zip(new_points[i], (0,0)))

    plt.scatter(*zip(original_center), color="Orange")
    plt.scatter(X, Y)
    plt.scatter(*zip(new_center), color="Red")
    plt.scatter([a[0] for a in new_points], [a[1] for a in new_points])
    plt.show()