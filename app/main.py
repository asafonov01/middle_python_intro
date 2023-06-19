import sys


def greeting(name: str) -> str:

    return 'Привет, {0}'.format(name.title())


if __name__ == '__main__':
    greeting(str(sys.argv[1]))