def uncovered_if(var=True):
    if var:
      return False
    else:
      return True

# V444444

def testing_v4():
    if a:
        return 3
    else:
        return 1

def fully_covered():
    # Added a change here
    return True

def uncovered():
    return True

