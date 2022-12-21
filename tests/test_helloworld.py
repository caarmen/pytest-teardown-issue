"""
Unit tests
"""
import pytest


class TestHelloWorld:

    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        yield
        print("teardown")

    def test_helloworld(self):
        assert True
