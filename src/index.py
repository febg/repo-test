def uncovered_if(var=True):
    if var:
      return False
    else:
      return True


def fully_covered():
    # Added a change here
    return True

def uncovered():
    return True

def uncovered2():
    a = 2
    b = 3
    c = a + b
    return True
