from potato_Lexer import *


def potato_open(path):
    try:
        file = open(path, 'r')
        return potato_ice(file.read().splitlines())
    except OSError:
        try:
            return potato_ice(path.splitlines())
        except:
            print('OSError')


def potato_ice(my_code):
    arr = [[" "]]*(len(my_code))
    r = 0
    for _ in my_code:
        arr[r] = [my_code[r]]
        r += 1
    return reception(arr)


def potato_run():
    return potato_open(input('>>> '))


print(potato_run())
