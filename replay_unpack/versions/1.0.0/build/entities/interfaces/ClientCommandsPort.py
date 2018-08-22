#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class ClientCommandsPort(object):
    
    g_onCmdResponse = EventHook()
    
    g_onCmdResponseExt = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (10000000000, 'onCmdResponse'),
            (10000000000, 'onCmdResponseExt'),
            
        ])
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


    # method size: 10000000000
    @unpack_func_args(['INT16', 'INT16', 'STRING'])
    def onCmdResponse(self, arg1, arg2, arg3):
        self.g_onCmdResponse.fire(self, arg1, arg2, arg3)

    # method size: 10000000000
    @unpack_func_args(['INT16', 'INT16', 'STRING', 'STRING'])
    def onCmdResponseExt(self, arg1, arg2, arg3, arg4):
        self.g_onCmdResponseExt.fire(self, arg1, arg2, arg3, arg4)


    ####################################
    #       PROPERTIES
    ####################################



    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)