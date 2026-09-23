import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    padding = "Z" * (8 - len(text))
    print(text + padding)

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)