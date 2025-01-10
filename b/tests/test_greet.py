"""Tests for the greet function."""
from b.greet import greet_b


def test_greet():
    """Test the greet function."""
    assert greet_b("World") == "Hello, World!"
    assert greet_b("Python") == "Hello, Python!" 
