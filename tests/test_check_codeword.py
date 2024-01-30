from lib.check_codeword import *

def test_check_codeword_correct_word():
    result = check_codeword('horse')
    assert result == 'Correct! Come in!'

def test_with_close_word():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_with_wrong_word():
    result = check_codeword('ants')
    assert result == 'WRONG!'