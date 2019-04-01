from domain import Properties as p

try:
    from cStringIO import StringIO
except:
    from io import StringIO    

class Node(object):

    # __id = None
    # __properties = None

    def __init__(self, nodeId, properties):
        self.nodeId = nodeId
        self.properties = p.Properties()
        self.properties.add_properties(properties)

    def to_string(self):
        buf = StringIO()
        buf.write("id ->" + str(self.nodeId))

        for k, v in self.properties.properties.items():
            buf.write( " " + k + " -> " + str(v))

        return  buf.getvalue()

    def add_property(self, key, value):
        self.properties.add_property(key, value)

    def getIdentity(self):
        return self.nodeId 


if __name__ == '__main__' :
    pass