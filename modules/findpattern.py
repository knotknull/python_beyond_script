#findpattern.py
import sys

# example of a generator function
# 
def grepfile(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line: 
                yield line.rstrip('\n')

if __name__ == "__main__":
    # get args from command line
    pattern, path = sys.argv[1], sys.argv[2]
    ## calls generator 
    for line in grepfile(pattern, path):
        print(line)
