'''
Will do a parse of a 2d obj file
(with only vertexes and faces)
'''

def get_data(filepath):
    '''
    Load vertexes and face data from an obj file
    return: (verts, faces)
        verts is a list of (x, y, z) coordinate tuples
        faces is a list of (a, b, c) tuples where a, b, c are points at index+1 in the verts list
    '''
    with open(filepath) as file:
        content = file.read()
        lines = content.split('\n')

    verts = []
    faces = []
    for line in lines:
        if line.startswith("v "):
            v, x, y, z = line.split(' ')
            point = tuple([float(a) for a in [x, y, z]])
            verts.append(point)

        elif line.startswith("f "):
            f, x, y, z = line.split(' ')
            point = remove_texture((x, y, z))
            faces.append(point)

    return (verts, faces)


def remove_texture(point):
    '''
    format line in obj file for face into vertex indeces
    '''
    out = []
    for a in point:
        out.append(int(a.split('//')[0]))

    return tuple(out)


def make_sets(verts, faces):
    '''
    Converts faces into list of (x, y, z) coordinates
    '''
    out = []
    for face in faces:
        a, b, c = face
        a -= 1
        b -= 1
        c -= 1
        
        edge = [verts[a], verts[b], verts[c]]
        out.append(edge)

    return out


def center(a, b, c):
    '''
    find center average on a plane
    '''
    x = (a[0] + b[0] + c[0]) / 3
    y = (a[1] + b[1] + c[1]) / 3
    z = (a[2] + b[2] + c[2]) / 3
    return (x, y, z)


def face_center(face):
    a, b, c = face
    out = center(a, b, c)

    return out


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

