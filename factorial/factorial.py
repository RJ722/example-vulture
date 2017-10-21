import sys

def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n

    """
    if n == 0:
        return 1
    return n * fact(n -1)


def unused_function():
    """
    This function does nothing.
    It is never called anywhere, hence, it is an example
    of dead code.
    """
    print("I am an example of dead code")
    return 0


def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))

