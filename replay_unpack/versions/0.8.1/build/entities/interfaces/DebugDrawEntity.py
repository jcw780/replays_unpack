#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class DebugDrawEntity(object):
    
    g_debugExec = EventHook()
    
    g_drawDebugLine = EventHook()
    
    g_drawDebugCircle = EventHook()
    
    g_drawDebugCross = EventHook()
    
    g_drawBoundingBox = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (10000000001, 'debugExec'),
            (257, 'drawDebugLine'),
            (193, 'drawDebugCircle'),
            (193, 'drawDebugCross'),
            (193, 'drawBoundingBox'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._methods:
                continue
            self._methods.append(item)
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################

# method size: 10000000001
    @unpack_func_args(['STRING', 'BLOB'])
    def debugExec(self, arg1, arg2):
        self.g_debugExec.fire(self, arg1, arg2)
# method size: 257
    @unpack_func_args(['VECTOR3', 'VECTOR3', 'UINT32', 'UINT32'])
    def drawDebugLine(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugLine.fire(self, arg1, arg2, arg3, arg4)
# method size: 193
    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'UINT32'])
    def drawDebugCircle(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugCircle.fire(self, arg1, arg2, arg3, arg4)
# method size: 193
    @unpack_func_args(['VECTOR3', 'FLOAT32', 'UINT32', 'UINT32'])
    def drawDebugCross(self, arg1, arg2, arg3, arg4):
        self.g_drawDebugCross.fire(self, arg1, arg2, arg3, arg4)
# method size: 193
    @unpack_func_args(['VECTOR3', 'VECTOR3'])
    def drawBoundingBox(self, arg1, arg2):
        self.g_drawBoundingBox.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################



    def get_summary(self):
        print('~' * 60)
        print('Entity name: ', self.__class__.__name__)
        print('Total entity client properties: {:>5}'.format(len(self._properties)))
        print('Total entity client methods: {:>5}'.format(len(self._methods)))

        print()
        print('Listing entity properties:')
        print('{:>4} {:>40}'.format('idx', 'property name'))
        for i, p in self.attributesMap.items():
            print('{:>4} {:>40}'.format(i, p))

        print()
        print('Listing entity methods:')
        print('{:>4} {:>40}'.format('idx', 'method name'))
        for i, p in self.methodsMap.items():
            print('{:>4} {:>40}'.format(i, p))
        print('~' * 60)
        print()
        print()


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)