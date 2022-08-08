import pytest

#A simple pytest fixture that can return an object, like an integer.
@pytest.fixture
def one():
    return 1

def test_we_are(one):
    assert one ==  1


#Fixtures modularization
@pytest.fixture
def me():
    return "me"

#This fixture requests the other
@pytest.fixture
def together(me):
    return "You and " + me


@pytest.fixture
def happy():
    return " are happy"

#This fixture requests two inputs from previous fixtures
@pytest.fixture
def complete(together, happy):
    return together + happy

def test_modular_complete(complete):
    assert complete == "You and me are happy"