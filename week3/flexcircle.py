from math import pi, sqrt
import sys

class FlexCircle(object):
    """
    Class that computes properties of a circle based 
    on either radius, area or perimeter
    """

    def __init__(self, r):
        """Constructs radius r"""
        self.set_radius(r)

    def set_area(self, a):
        """
        Assigns new value for area and
        updates radius and perimeter
        """
        self._area = self.set_data(a)
        self._radius = sqrt(self._area/pi)
        self._perimeter = 2*pi*self._radius

    def set_perimeter(self, p):
        """
        Assigns new value for perimeter and
        updates radius and area
        """
        self._perimeter = self.set_data(p)
        self._radius = self._perimeter/(2*pi)
        self._area = pi*self._radius**2

    def set_radius(self, r):
        """
        Assigns new value for radius and
        updates area and perimeter
        """
        self._radius = self.set_data(r)
        self._perimeter = 2*pi*self._radius
        self._area = pi*self._radius**2 

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter

    def get_radius(self):
        return self._radius

    def set_data(self, data):
        """
        Check if given attribute is a number,
        if not, an error message is printed
        """
        if isinstance(data, (float,int)):
             return data
        else:
            print 'Attribute value must be a number!'
            sys.exit(1)
            

    area      = property(fget=get_area,      fset=set_area)
    perimeter = property(fget=get_perimeter, fset=set_perimeter)
    radius    = property(fget=get_radius,    fset=set_radius)

        
if __name__ == '__main__':
    c = FlexCircle(r=10)
    print c.area
    c.perimeter = 5
    print c.radius
    print c.area
