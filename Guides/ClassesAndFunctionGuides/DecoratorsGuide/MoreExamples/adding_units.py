import math
import pint
import functools


# pint allows for unit conversion


def set_unit(unit):
    """Register a unit on a function"""

    def decorator_set_unit(func):
        func.unit = unit
        return func

    return decorator_set_unit


@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius ** 2 * height


print(f'{volume(1, 2):.2f} {volume.unit}')

ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)

print(vol)
print(vol.to('cubic inches'))
print(vol.to('gallons').m)
# m -> magnitude only


# can use pint to return a quantity with a use_unit decorator
def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()

    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)

        return wrapper_use_unit

    return decorator_use_unit


@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration


bolt = average_speed(100, 9.58)
print(bolt)
