import parser
from tqdm import tqdm
import time
import numpy as np
import math

def project_to_face(point, face):
    x1, y1, z1 = point
    a, b, c, d = plane

    # find point on plane perp to point
    k =(-a * x1-b * y1-c * z1-d)/float((a * a + b * b + c * c)) 
    x2 = a * k + x1
    y2 = b * k + y1
    z2 = c * k + z1

    mid = (x2, y2, z2)
    return mid


def point_in_face(point, face):
    x, y, z = map(list, zip(*face))
    
    valid_x = point[0] > min(x) and point[0] < min(x)
    valid_y = point[1] > min(y) and point[1] < min(y)
    valid_z = point[2] > min(z) and point[2] < min(z)

    return (valid_x and valid_y and valid_z)


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


def translate(point, translation):
    # Build the translation matrix and vector to multiply by
    trans_matr = np.identity(len(point)+1, dtype=float)
    vect = np.ones(len(point)+1, dtype=float)
    for i in range(len(point)):
        trans_matr[i][-1] = translation[i]
        vect[i] = point[i]

    m = np.matmul(trans_matr, vect)
    out = np.resize(m, (1, 3)).tolist()[0]
    return out


def translate_all(points, translation):
    out = []
    for point in points:
        out.append(tuple(translate(point, translation)))

    return out


def invert(point):
    out = []
    for x in point:
        out.append(-x)
    return out


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
    theta = math.atan(m)

    return theta


def xy_rotation(vert, angle):
    c, s = math.cos(angle), math.sin(angle)
    matr = np.array(((c, -s), (s, c)))
    v = np.array((vert[0], vert[1]))
    
    out = np.matmul(matr, v)
    out = out.tolist()
    out.append(vert[2])
    return out


def xy_rotate_all(verts, angle):
    out = []
    for vert in verts:
        out.append(tuple(xy_rotation(vert, angle)))

    return out


start = time.time()

# Load data
source_file = "../../models/simplified/simplified_900/simplified_900.obj"
verts, faces = parser.get_data(source_file)
og_verts = verts[:]
og_sets = parser.make_sets(verts, faces)
center = center_of_mass(verts)

# print(verts[:10])
# print(faces[:10])
# print(sets[:10])
print(len(verts), len(faces))


# Make source point
source = (30, 30, 50)

# Translate all points to make source origin
verts = translate_all(verts, invert(source))

# Rotate on xy plane to center model
center = center_of_mass(verts)
angle = xy_angle(center)
print(center)
print(angle, math.degrees(angle))

verts = xy_rotate_all(verts, math.degrees(angle))
center = center_of_mass(verts)
angle = xy_angle(center)
print(center)
print(angle, math.degrees(angle))


# Rotate on yz plane to center model

# Project onto 2d plane


# Chart faces
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Chart vertexes
sets = parser.make_sets(verts, faces)
print("Charting faces")
for face in tqdm(sets):
    x, y, z = map(list, zip(*face))
    ax.plot(x, y, z, color='b', marker='o', markersize=1, linestyle='-', linewidth=0.3)

for face in tqdm(og_sets):
    x, y, z = map(list, zip(*face))
    ax.plot(x, y, z, color='r', marker='o', markersize=1, linestyle='dashed', linewidth=0.3)

# # Chart lines to centers
# print("Drawing lines")
# for face in tqdm(sets):
#     cent = parser.face_center(face)
#     # Check that line is not running into a collision with another face
#     plt.plot(*zip(source, cent), linestyle='dotted', color='orange', alpha=0.5)

duration = time.time() - start
print(f"duration: {duration}")
plt.show()
