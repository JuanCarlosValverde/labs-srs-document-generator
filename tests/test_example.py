"""
Example test file for the SRS Document Generator
"""
from src.main import hello_world


def test_hello_world():
    """Test hello_world function"""
    result = hello_world()
    assert result == "Hello, World!"
