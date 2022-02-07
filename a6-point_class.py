class Point(object):

    #Define constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __repr__(self):
        return "Point({}, {})".form(self.x, self.y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)