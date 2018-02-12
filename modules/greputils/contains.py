def contains(pattern, path):
    with open(path) as handler:
        for line in handle:
            if pattern in line: 
                return True
    return False

def containsi(pattern, path):
    pattern = pattern.lower()
    with open(path) as handler:
        for line in handle:
            if pattern in line.lower(): 
                return True
    return False
