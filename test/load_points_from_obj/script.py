
def remove_texture(point):
    out = []
    for a in point:
        out.append(float(a.split('//')[0]))

    return tuple(out)


# Load file content
file_path = "/Users/ethanbolton/Desktop/ear_reflection/models/trimmed/trimmed.obj"
with open(file_path) as file:
    content = file.read()
    lines = content.split('\n')


# Build object features
verts = []
normals = []
faces = []
for line in lines:
    if line.startswith("v "):
        v, x, y, z = line.split(' ')
        point = tuple([float(a) for a in [x, y, z]])
        verts.append(point)

    elif line.startswith("vn "):
        v, x, y, z = line.split(' ')
        point = tuple([float(a) for a in [x, y, z]])
        normals.append(point)

    elif line.startswith("f "):
        f, x, y, z = line.split(' ')
        point = (x, y, z)
        faces.append(remove_texture(point))

# print(faces)


# Draw points in 2d
import matplotlib.pyplot as plt

x, y, z = [], [], []
for a in verts:
    x.append(a[0])
    y.append(a[1])
    z.append(a[2])

plt.scatter(x, y, s=0.1)
plt.show()