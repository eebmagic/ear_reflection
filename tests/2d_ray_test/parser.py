'''
Will do a parse of a 2d obj file
(with only vertexes and faces)
'''

def get_data(filepath):
    with open(filepath) as file:
        content = file.read()
        lines = content.split('\n')

    verts = []
    faces = []
    for line in lines:
        if line.startswith("v "):
            v, x, y = line.split(' ')
            point = tuple([int(a) for a in [x, y]])
            verts.append(point)

        elif line.startswith("f "):
            f, x, y = line.split(' ')
            point = tuple([int(a) for a in [x, y]])
            faces.append(point)

    return (verts, faces)


def make_sets(verts, faces):
    out = []
    for face in faces:
        a, b = face
        a -= 1
        b -= 1
        
        edge = {verts[a], verts[b]}
        out.append(edge)

    return out


if __name__ == "__main__":
    v, f = get_data("simple_ear.obj")
    s = make_sets(v, f)
    print(s)

    x, y = map(list, zip(*v))

    # import matplotlib.pyplot as plt
    # plt.plot(x, y)
    # plt.show()