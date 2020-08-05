import parser
from tqdm import tqdm

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
    plt.plot(*zip(source, cent), linestyle='dotted', color='orange', alpha=0.5)

plt.show()