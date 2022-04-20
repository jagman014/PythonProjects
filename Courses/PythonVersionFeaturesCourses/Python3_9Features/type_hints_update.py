# 3.9 introduces annotated type hints
# add both type hints and meta information
from typing import Annotated, get_type_hints

# 3.8 annotation example
FPS_TO_MPH = 3600 / 5280


def speed(distance:'feet', time:'seconds') -> 'miles per hour':
    return distance / time * FPS_TO_MPH

print(speed(10, 2))
print(speed.__annotations__)

# 3.8 type hints example
def speed_1(distance:float, time:float) -> float:
    return distance / time * FPS_TO_MPH


print(speed_1(10, 2))
print(speed_1.__annotations__)

# 3.9 allows for both
Feet = Annotated[float, 'feet']
MPH = Annotated[float, 'miles per hour']


def speed_2(distance:Feet, time:Annotated[float, 'seconds']) -> MPH:
    return distance / time * FPS_TO_MPH


print(speed_2(10, 2))
print(speed_2.__annotations__)
# from annotations dictionary can extract meta data
print(speed_2.__annotations__['distance'].__metadata__)
# can also use typing.get_type_hints
print(get_type_hints(speed_2))
print(get_type_hints(speed_2, include_extras=True))


# can create an annotation 'factory'
class AnnotationFactory:
    def __init__(self, type_hint):
        self.type_hint = type_hint
    
    def __getitem__(self, key):
        if isinstance(key, tuple):
            return Annotated[(self.type_hint, ) + key]
        
        return Annotated[self.type_hint, key]
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.type_hint})'


Float = AnnotationFactory(float)


def speed_3(distance:Float["feet"], time:Float['seconds']) -> Float['MPH']:
    return distance / time * FPS_TO_MPH
