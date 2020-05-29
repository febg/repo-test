import pytest
import index
import index2

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True

def test_new_new():
    assert index.new_new() == False

def test_new_func():
    assert index.new_func() == True
