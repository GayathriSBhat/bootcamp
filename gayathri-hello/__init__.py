import sys

def say_hello():
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(f"Hello {name}")

if __name__ == "__main__":
    say_hello()
