from mimetypes import init

#Type class for Employee object checking
class Typed(object):
    expected_type = object

    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, cls):
        return instance.__dict__(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("'{}' must be {}".format(self.name, self.expected_type))
        instance.__dict__[self.name] = value
    
class Integer(Typed):
    expected_type = init

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str