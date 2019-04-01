import itertools
try:
    from cStringIO import cStringIO
except:
    from io import StringIO

class Properties(object):

     
    def __init__(self):
        self.properties = {}

    def add_properties(self, properties):
        self.properties = properties

    def add_property(self, key, value):
        self.properties[key] = value 
        

    def get_value(self, key):
        return self.properties[key]

    def to_string(self):
        buf = StringIO()       
        for k, v in iter(self.properties.items()):
            buf.write(str(k) + ' -> ' + str(v))

        return buf.getvalue()
