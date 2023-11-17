from potato_Lexer import *


# - Run - #
def p(i):
    if i == 'end':
        quit()
    else:
        return PotatoHi(i).potato1()


if __name__ == '__main__':
    while T:
        print(p(input('>>> ')))

