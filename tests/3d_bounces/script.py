import parser
from tqdm import tqdm
import time

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



start = time.time()

# Load data
source_file = "../../models/simplified/simplified_900/simplified_900.obj"
verts, faces = parser.get_data(source_file)
sets = parser.make_sets(verts, faces)

# print(verts[:10])
# print(faces[:10])
# print(sets[:10])
print(len(verts), len(faces))
print(len(sets))


# Make source point
source = (30, 30, 50)


# Chart faces
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Chart vertexes
print("Charting faces")
for face in tqdm(sets):
    x, y, z = map(list, zip(*face))
    ax.plot(x, y, z, color='b', marker='o', markersize=1, linestyle='-', linewidth=0.3)

# Chart lines to centers
print("Drawing lines")
for face in tqdm(sets):
    cent = parser.face_center(face)
    # Check that line is not running into a collision with another face
    plt.plot(*zip(source, cent), linestyle='dotted', color='orange', alpha=0.5)

duration = time.time() - start
print(f"duration: {duration}")
plt.show()
