import index2

def test_uncovered_if():
    assert index2.uncovered_if2() == False

def test_fully_covered():
    assert index2.fully_covered2() == True
