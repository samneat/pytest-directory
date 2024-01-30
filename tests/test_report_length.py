from lib.report_length import *

def test_report_length_return_length():
    result = report_length('camel')
    assert result == 'This string was 5 characters long.'

def test_with_empty_string():
    result = report_length('')
    assert result == 'This string was 0 characters long.'