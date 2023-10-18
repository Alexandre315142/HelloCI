# import library

import pytest
from src.calculateArea import areaSquare


# validation result
def test_areaSquare():
    """_summary_
    """
    assert areaSquare(2) == 4
    assert areaSquare(2.5) == 6.25

# validate negative param   
def test_areaSquare_negative():
    """_summary_
    """
    with pytest.raises(TypeError):
        areaSquare(-2)

#validate string param
def test_areaSquare_string():
    """_summary_
    """
    with pytest.raises(TypeError):
        areaSquare("2")

# validate list param
def test_areaSquare_list():
    """_summary_
    """
    with pytest.raises(TypeError):
        areaSquare([2])