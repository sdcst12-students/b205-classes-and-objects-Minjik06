"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""

class rectPrism:
    length=0
    width=0
    height=0

    def __init__(self, l=0,w=0,h=0):
        # note you will need to specify more input parameters
        self.length = l
        self.width = w
        self.height = h
        pass

    def volume(self):
        if self.length<=0 or self.width<=0 or self.height<=0:
            vol=None
        else:
            vol=self.length*self.width*self.height
        return vol
    
    def surfaceArea(self):
        if self.length<=0 or self.width<=0 or self.height<=0:
            surfaceA = None
        else:
            surfaceA = (2*self.length*self.width)+(2*self.length*self.height)+(2*self.width*self.height)
        return surfaceA

# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

"""b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea == 6"""

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None


""" def __init__(self, l=0,w=0,h=0):
        # note you will need to specify more input parameters
        if l > 0:
            self.length = l
        if w > 0:
            self.width = w
        if h > 0:
            self.height = h
        if l<=0 or w<=0 or h<=0:
            self.height = h
            self.width = w
            self.length = l"""