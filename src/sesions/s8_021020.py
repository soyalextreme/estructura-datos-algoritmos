from lib.decorators import cronometer


@cronometer
def main():
    for i in range(200):
        print("*")


def hola():
    main()
