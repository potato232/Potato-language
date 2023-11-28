from potato_tokens import *


class PotatoP:
    def __init__(self, data):
        self.p1 = data

    def potato(self):
        return PotatoMath(potato_clear(self.p1)).math()


class PotatoMath:
    def __init__(self, data):
        self.p1 = data

    def math(self):
        clear_data = self.p1
        # - bracket - #
        while 'LB' in clear_data or 'RB' in clear_data:
            clear_data = potato0(clear_data)

        # - power - #
        while 'POW' in clear_data:
            clear_data = potato1(clear_data)

        # - mul or div or div2 - #
        while 'MUL' in clear_data or 'DIV' in clear_data or 'FLOAT_DIV' in clear_data:
            clear_data = potato2(clear_data)

        # - plus or minus - #
        while 'PLUS' in clear_data or 'MINUS' in clear_data:
            clear_data = potato3(clear_data)

        # - Logical equations - #
        while 'NOT' in clear_data or 'LESS' in clear_data or 'GREATER' in clear_data or 'EQUALS' in clear_data:
            clear_data = potato4(clear_data)

        return list(clear_data)


# - bracket - #
def potato0(data, func=N):
    func = func if func != N else []
    if 'LB' in data or 'RB' in data:
        r1 = 0
        while True:
            if data[r1] == 'RB':
                break
            r1 += 1
        r2 = r1
        while True:
            if data[r2] == 'LB':
                break
            r2 += 1
        if type(data[r1-1]) == PotatoV:
            data[r1-1] = 'hi'
            data[r1:r2+1] = ''
        else:
            data[r1:r2+1] = PotatoMath(data[r1+1:r2]).math()
        return data
    return data


# - power - #
def potato1(data):
    if 'POW' in data:
        r = 0
        for d in data:
            r += 1
            if d == 'POW':
                data[r] = data[r-2] ** data[r]
                data[r-2:r] = ''
    return data


# - mul or div or div2 - #
def potato2(data):
    r = 0
    for d in data:
        r += 1
        if d == 'MUL':
            data[r] = data[r-2] * data[r]
            data[r-2:r] = ''
        if d == 'DIV':
            data[r] = data[r-2] / data[r]
            data[r-2:r] = ''
        if d == 'FLOAT_DIV':
            data[r] = data[r-2] // data[r]
            data[r-2:r] = ''
    return data


# - plus or minus - #
def potato3(data):
    r = 0
    for d in data:
        r += 1
        if d == 'PLUS':
            if type(data[r-2]) in [int, float] and type(data[r]) in [int, float]:
                data[r] = data[r-2] + data[r]
            else:
                data[r] = str(data[r-2]) + str(data[r])
            data[r-2:r] = ''
        if d == 'MINUS':
            if type(data[r-2]) in [int, float] and type(data[r]) in [int, float]:
                data[r] = data[r-2] - data[r]
            elif type(data[r-2]) in [int, float] or type(data[r]) in [int, float]:
                try:
                    data[r] = str(int(data[r-2]) - int(data[r]))
                except:
                    data[r] = ango_three(str(data[r - 2]), str(data[r]))
            else:
                data[r] = ango_three(str(data[r - 2]), str(data[r]))
            data[r-2:r] = ''
    return data


# - Logical equations - #
def potato4(data):
    r = 0
    for d in data:
        r += 1
        if d == 'NOT':
            data[r] = PotatoT('TRUE') if data[r-2] != data[r] else PotatoT('FALSE')
            data[r-2:r] = ''
        if d == 'EQUALS':
            data[r] = PotatoT('TRUE') if data[r-2] == data[r] else PotatoT('FALSE')
            data[r-2:r] = ''
        if d == 'LESS':
            data[r] = PotatoT('TRUE') if data[r-2] < data[r] else PotatoT('FALSE')
            data[r-2:r] = ''
        if d == 'GREATER':
            data[r] = PotatoT('TRUE') if data[r-2] < data[r] else PotatoT('FALSE')
            data[r-2:r] = ''
    return data


def ango_three(w1, w2):
    if w2 in w1:
        try:
            out = ''
            r = 0
            while r < len(w1):
                if w1[r] == w2[0]:
                    if w1[r:len(w2)+r] == w2:
                        out += w1[r+len(w2):]
                        return out
                out += w1[r]
                r += 1
            return out
        except:
            pass
    return w1


# - clear data - #
def potato_clear(data):
    out = []
    for x in data:
        if ':' in x:
            r = 0
            for _ in x:
                match x[:r + 1]:
                    # if x[r+1] is INT #
                    case 'INT':
                        out.append(int(x[r+2:]))
                    # if x[r+1] is FLOAT #
                    case 'FLOAT':
                        out.append(float(x[r+2:]))
                    # if x[r+1] is STR #
                    case 'STRING':
                        out.append(str(x[r+2:]))
                    # if x[r+1] is bool
                    case 'BOOL':
                        out.append(str(x[r+2:]))
                    # if else x[r+1]
                    case 'VAR':
                        out.append(PotatoV(x[r+2:]))
                    case 'KEYWORD':
                        out.append(PotatoK(x[r+2:]))
                r += 1
        else:
            out.append(x)
    return out
