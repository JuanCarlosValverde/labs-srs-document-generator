"""
Example test file for the SRS Document Generator
"""
import pytest


def test_example():
    """Example test to ensure pytest works"""
    assert True


def test_google_cloud_import():
    """Test that Google Cloud libraries can be imported"""
    try:
        from google.cloud import firestore
        from google.cloud import storage
        from google.auth import default
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import Google Cloud libraries: {e}")
