#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class AtbaOwner(object):
    
    g_shootATBAGuns = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._atbaTargets = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        for item in [
            (10000000000, 'atbaTargets'),
            
        ]:
            # in order to avoid duplicates same as BigWorld does
            if item in self._properties:
                continue
            self._properties.append(item)

        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        for item in [
            (33, 'shootATBAGuns'),
            
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

# method size: 33
    @unpack_func_args(['UINT32'])
    def shootATBAGuns(self, arg1):
        self.g_shootATBAGuns.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def atbaTargets(self):
        return self._atbaTargets

    @atbaTargets.setter
    def atbaTargets(self, value):
        self._atbaTargets, = unpack_variables(value, ['ATBA_TARGETS'])


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