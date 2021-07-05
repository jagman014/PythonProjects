# getting a bit
def get_bit(value, bit_index):
    """
    takes in a value and bit index, then return either
    2 ** bit_index or zero depending if the bit is on / off
    """
    return value & (1 << bit_index)


# get normalised bit
def get_norm_bit(value, bit_index):
    """
    takes in a value and a bit index, then returns 
    the value at that bit index, 1 or 0
    """
    return (value >> bit_index) & 1


# setting a bit
def set_bit(value, bit_index):
    """
    sets the bit at the given bit index to 1 in the given value
    """
    return value | (1 << bit_index)


# resetting a bit
def reset_bit(value, bit_index):
    """
    resets the bit at the given bit index to 0 in the given value
    """
    return value & ~(1 << bit_index)


# toggling a bit
def toggle_bit(value, bit_index):
    """
    toggles the bit at the given index from 1 to 0 or vice verca
    """
    return value ^ (1 << bit_index)
