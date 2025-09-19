"""
Example test file for the SRS Document Generator
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.main import hello_world


def test_hello_world():
    """Test hello_world function"""
    result = hello_world()
    assert result == "Hello, World!"
