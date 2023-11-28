from potato_Lexer import *


# - Run - #
def p(i):
    if i == 'end':
        quit()
    else:
        return PotatoHi(i).potato1()


def potato_ice(my_code):
    arr = [[" "]]*(len(my_code))
    r = 0
    for _ in my_code:
        arr[r] = [my_code[r]]
        r += 1
    return reception(arr)


if __name__ == '__main__':
    c = """
    potato_var x = 1 :
    potato_var y = 1 :
    potato_if (x == y) :
    {
    print(x + y) :
    }
    """

    print(p(c))

    while T:
        code = p(input('>>> '))
        print(code)
"""
    try:
        while T:
           code = p(input('>>> '))
           print(code)
    except:
        print(PotatoE('potato', 'SyntaxError', 'u can\'t speak with potato').potato_error())
"""
