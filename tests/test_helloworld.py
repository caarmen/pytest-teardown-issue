"""
Unit tests
"""

from helloworld.helloworld import greeting


def test_helloworld():
    """
    One test
    """
    assert greeting() == "hello world"
