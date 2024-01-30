from lib.greet import *

def test_greet_return_hello_name():
    result = greet('Sam')
    assert result == 'hello, Sam'