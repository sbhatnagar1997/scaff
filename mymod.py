# This is a module - I want to stop people executing it directly
import sys

# If you are importing things, the value of main will be mymod
if __name__ == '__main__':
    sys.exit()

def myfunc():
    pass

print(__name__)
