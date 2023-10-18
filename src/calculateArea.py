# import library

#****#

# This function has role to calculate area
def areaSquare(length : float) -> float:
    """ this function to calculate square area

    Args:
        length (float): param1

    Returns:
        float: area result
    """
    if not isinstance(length, float) or length <=0:
        raise TypeError("Check the parameter type please!")
    
    return length * length