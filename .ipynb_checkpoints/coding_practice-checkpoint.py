#maximum value like INT_MAX in python 
INT_MAX = 2**31 - 1
#minimum value like INT_MIN in python
INT_MIN = -2**31
def max_value():
    """Returns the maximum value like INT_MAX in Python."""
    return INT_MAX
def min_value():
    """Returns the minimum value like INT_MIN in Python."""
    return INT_MIN
def is_valid_index(index, length):
    """Checks if the index is valid for a given length."""
    return 0 <= index < length
def is_valid_index_range(start, end, length):
    """Checks if the index range is valid for a given length."""
    return 0 <= start < end <= length       