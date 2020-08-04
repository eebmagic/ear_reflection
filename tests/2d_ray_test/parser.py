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
        
        edge = [verts[a], verts[b]]
        out.append(edge)

    return out


def center(a, b):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return (x, y)


def make_plane(a, b):
    pass


if __name__ == "__main__":
    # Load data from ear obj
    v, f = get_data("simple_ear.obj")
    faces = make_sets(v, f)
    print(faces)

    source = (0.5, 6)




    ### Chart data
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot()

    # plot ray attempts
    for face in faces:
        cent = center(face[0], face[1])
        plt.plot(*zip(source, cent), linestyle='dashed', color='orange')

    # plot ear faces
    x, y = map(list, zip(*v))
    plt.plot(x, y, marker='o')

    # plot source point
    plt.plot(*zip(source), marker='o')

    

    plt.show()

