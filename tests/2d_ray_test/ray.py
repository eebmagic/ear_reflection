def slope(a, b):
    '''
    Return the slope:
        a - tuple of first point
        b - tuple of second point
    '''
    assert type(a) == tuple and type(b) == tuple, "a and b must be tuple"
    assert len(a) == 2 and len(b) == 2, "tuples must only be 2d"
    y = b[1] - a[1]
    x = b[0] - a[0]
    s = y / x

    return s


def get_from_mid(point, mid):
    '''
    Get the point on the other side of the mid point
        point - the point to one side of the midpoint
        mid - the midpoint
    '''
    assert type(a) == tuple and type(b) == tuple, "point and midpoint must be tuple"
    assert len(a) == 2 and len(b) == 2, "point tuples must only be 2d"
    
    x = (2 * mid[0]) - point[0]
    y = (2 * mid[1]) - point[1]
    return (x, y)


def make_plane(a, b, c):
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
    print "equation of plane is ", 
    print a, "x +", 
    print b, "y +", 
    print c, "z +", 
    print d, "= 0."


class Ray:
    def __init__(self, pos, bounces=0):
        assert type(pos) == tuple, "Ray position should be given as a tuple"
        assert len(pos) == 2, "Ray position tuple should be 2d (x, y)"
        self.position = pos
        self.bounces = bounces


    def bounce(plane):
        reflected_position = 
        new = Ray(self.pos, bounces=self.bounces+1)



if __name__ == "__main__":
    r = Ray((1, 2))
    print(r.position)