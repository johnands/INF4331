from math import pi

class Circle:
    """
    Class that computes area and perimeter of a circle
    for a given radius
    """

    def __init__(self, r):
        """Constructs the radius r"""
        self.r = r

    def area(self):
        """Computes area of circle"""
        return pi*self.r**2
 
    def perimeter(self):
        """Computes perimeter of circle"""
        return 2*pi*self.r

if __name__ == '__main__':
    c = Circle(r=10)
    print 'Area of cirle with r = %.1f : %.1f' % (c.r, c.area())
    print 'Perimeter of cirle with r = %.1f: %.1f' % (c.r, c.perimeter())
