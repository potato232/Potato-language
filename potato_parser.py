from potato_tokens import *


# input = ['int : 1', 'plus', 'int : 1']
class PotatoP:
    def __init__(self, potato):
        # potato = ['type':'value', 'type':'value']
        self.potato: list = potato

        # potato 1
        self.p1: int = 0
        self.p2: str = self.potato[self.p1]
        self.p3: bool = True

        # potato 2
        self.p4: int = 0
        self.p5: str = self.potato[self.p3]
        self.p6: bool = True

    # potato_n1 = next in list:potato1
    def potato_n1(self):
        if self.p1 < len(self.potato):
            self.p2 = self.potato[self.p1]
            self.p1 += 1
        else:
            self.p3 = F

    # potato_n2 = next in potato1
    def potato_n2(self):
        if self.p4 < len(self.potato):
            self.p5 = self.potato[self.p4]
            self.p4 += 1
        else:
            self.p6 = F

    # - potato - #
    # - potato is stop work here - #
    def potato_math(self):
        arr1 = self.potato_clear(self.p2)
        _arr2 = []
        _r1 = 0
        while self.p3:
            if LB in arr1:
                pass
            if POW in arr1:
                pass
            if MUL in arr1 or DIV in arr1 or DIV2 in arr1:
                pass
            if PLUS in arr1 or MIN in arr1:
                pass

            # -- is not working currently -- #
            if EQUAL in arr1 or NOT in arr1 or LESS in arr1 or GRE in arr1:
                pass
            # -- is not working currently -- #

            _r1 += 1
            self.potato_n1()
    # - potato is stop work here - #

    def potato_clear(self, data):
        _ = self.p2
        out = []
        for x in data:
            if ':' in x:
                r = 0
                for _ in x:
                    match x[r + 1:]:
                        case 'INT':
                            out.append(int(x[:r]))
                        case 'FLOAT':
                            out.append(float(x[:r]))
                        case 'STRING':
                            out.append(str(x[:r]))
                        case 'BOOL':
                            out.append(str(x[:r]))
                        case 'POTATO':
                            out.append(x[:r])
                    r += 1
            else:
                out.append(x)
        return out
