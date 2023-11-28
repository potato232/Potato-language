from potato_tokens import *
from potato_parser import *


class PotatoE:
    def __init__(self, c, t=N, i=N):
        self.p1 = c
        self.p2 = t if t != N else 'Error'
        self.p3 = i if i != N else 'in potato'

    def potato_error(self):
        return f'>>> {self.p1} <<< \n {self.p2} : {self.p3}'


class PotatoHi:
    def __init__(self, i):
        self.p1: str = ' '+i+' '
        self.p2: int = 0
        self.p3 = F

        self.potato_next()

    def potato_next(self):    # potato next
        if self.p2 < len(self.p1):
            self.p3 = self.p1[self.p2]
            self.p2 += 1
        else:
            self.p3 = F

    def potato1(self):     # potato B1
        arr = []
        while self.p3:
            if self.p3 == ' ':  # if potato is null
                self.potato_next()
            else:               # if potato is not null
                # if is character
                if self.p3 in POTATO_TOL:
                    arr.append(str(self.potato_tol()))
                    self.potato_next()
                # if is number
                elif self.p3 in POTATO_NUM:
                    arr.append(str(self.potato_num()))
                    self.potato_next()
                # if is quotation mark
                elif self.p3 in Q:
                    arr.append(str(self.potato_str()))
                    self.potato_next()
                # potato_else
                else:
                    arr.append(str(self.potato_else()))
                    if self.p3 not in POTATO_TOL:
                        self.potato_next()
        return potato_out(arr)

    # - potato - #
    def potato_tol(self):   # if potato in POTATO_TOL
        match self.p3:
            case '+':
                return PotatoT(PLUS)
            case '-':
                return PotatoT(MIN)
            case '*':
                return PotatoT(MUL)
            case '/':
                return PotatoT(DIV)
            case ',':
                return PotatoT(COMMA)
            case '(':
                return PotatoT(RB)
            case ')':
                return PotatoT(LB)
            case '!':
                return PotatoT(NOT)
            case '=':
                return PotatoT(BE)
            case ':':
                return PotatoT(COLON)
            case '<':
                return PotatoT(LESS)
            case '>':
                return PotatoT(GRE)
            case '{':
                return PotatoT(DO)
            case '}':
                return PotatoT(END)
        return PotatoT(TT_POTATO_POT, self.p3)

    def potato_num(self):
        arr, o = [], ''
        f = F

        # - 1 - #
        while self.p3:
            if self.p3 in POTATO_NUM or self.p3 == '.':
                arr.append(self.p3)
                self.potato_next()
            else:
                break
        # arr = [n1, n2, n3, ...] #

        # - 2 - #
        for i in arr:
            if i == '.':
                if f:
                    break
                f = T
            o += i
        # o = arr[1] + arr[2] + ... #

        # - 3 - #
        if f:
            return PotatoT(TT_POTATO_FLT, o)
        else:
            return PotatoT(TT_POTATO_INT, o)

    def potato_str(self):
        def w(q):
            o: str = ''
            while self.p3:
                self.potato_next()
                if self.p3 == q:
                    break
                o += self.p3
            return o
        return PotatoT(TT_POTATO_STR, w(self.p3))

    def potato_else(self):
        def p(i: str):
            if i in POTATO_BOL:
                return PotatoT(TT_POTATO_BOL, i)
            if i in POTATO_KEY_WORD:
                return PotatoT(TT_POTATO_KEY, i)
            return PotatoT(TT_POTATO_POT, i)
        o: str = ''
        while self.p3:
            pa = self.p3 == ' '
            if self.p3 in POTATO_TOL or pa:
                del pa
                return p(o)
            if self.p3 in Q or pa:
                del pa
                return p(o)
            o += self.p3
            self.potato_next()
        return p(o)

    def potato_e(self, c, t=N, i=N):
        t: str = t if t != N else 'Error'
        i: str = i if i != N else 'in potato'
        self.potato_next()
        return PotatoE(c, t, i).potato_error()


# potato is stop here #
def potato_out(data):
    r = 0
    for i in data:
        # == ** // #
        if str(i) in [MUL, DIV, BE]:
            i = str(i)
            if i == MUL:
                if str(data[r+1]) == MUL:
                    data[r] = POW
                    data.pop(r+1)
            elif i == DIV:
                if str(data[r+1]) == DIV:
                    data[r] = DIV2
                    data.pop(r+1)
            elif i == BE:
                if str(data[r+1]) == BE:
                    data[r] = EQUAL
                    data.pop(r+1)
        r += 1
    return PotatoP(data).potato()


def reception(data):
    r = 0
    while r < len(data):
        i = data[r]
        data[r] = PotatoHi(i[0]).potato1()
        r += 1
    return data
