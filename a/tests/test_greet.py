"""Tests for the greet function."""
from a.greet import greet_a


def test_greet():
    """Test the greet function."""
    assert greet_a("World") == "Hello, World!"
    assert greet_a("Python") == "Hello, Python!" 
