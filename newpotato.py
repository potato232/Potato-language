def potato_clear(data):
    out = []
    for x in data:
        if ':' in x:
            r = 0
            for _ in x:
                match x[r + 1:]:
                    # if x[r+1] is INT #
                    case 'INT':
                        out.append(int(x[:r]))
                    # if x[r+1] is FLOAT #
                    case 'FLOAT':
                        out.append(float(x[:r]))
                    # if x[r+1] is STR #
                    case 'STRING':
                        out.append(str(x[:r]))
                    # if x[r+1] is bool
                    case 'BOOL':
                        out.append(str(x[:r]))
                    # if else x[r+1]
                    case 'POTATO':
                        out.append(x[r])
                    case 'KEYWORD':
                        out.append(x[r])
                r += 1
        else:
            out.append(x)
    return out


def potato_1():
    pass


def potato_bracket(arr):
    if 'LB' in arr or 'RB' in arr:
        r2 = 0
        while True:
            if arr[r2] == 'RB':
                break
            r2 += 1
        r3 = r2
        while True:
            if arr[r3] == 'LB':
                break
            r3 -= 1
        arr[r3:r2+1] = '1'
        return arr
    return arr


# input = [5, power, 2] == 25
# input -> [5, plus, LB, 1, MIN, 5, RB]
