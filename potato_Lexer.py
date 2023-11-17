from potato_tokens import *


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
                #
                if self.p3 in POTATO_TOL:
                    arr.append(self.potato_tol())
                    self.potato_next()
                elif self.p3 in POTATO_NUM:
                    arr.append(self.potato_num())
                    self.potato_next()
                elif self.p3 in Q:
                    arr.append(self.potato_str())
                    self.potato_next()
                else:
                    self.potato_else()
                    self.potato_next()
        return arr

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
            case '^':
                return PotatoT(POW)
            case '√':
                return PotatoT(SQRT)
            case ',':
                return PotatoT(COMMA)
            case '(':
                return PotatoT(RB)
            case ')':
                return PotatoT(LB)
            case '.':
                return PotatoT(DOT)
            case '[':
                return PotatoT(BR)
            case ']':
                return PotatoT(BL)

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
            o = ''
            while self.p3:
                self.potato_next()
                if self.p3 == q:
                    break
                o += self.p3
            return o
        return PotatoT(TT_POTATO_STR, w(self.p3))

    def potato_else(self):
        
        if False:
            pass
        else:
            return self.potato_e(self.p1[self.p2 - 1])

    def potato_e(self, c, t=N, i=N):
        t = t if t != N else 'Error'
        i = i if i != N else 'in potato'
        self.potato_next()
        return PotatoE(c, t, i).potato_error()
