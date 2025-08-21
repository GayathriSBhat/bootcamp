import sys
def say_hello():
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(f"Hello {name}")
