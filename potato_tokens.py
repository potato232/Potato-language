
POTATO_KEY_WORD = ['potato_if', 'potato_var', 'potato_break', 'potato_loop',
                   'potato_do', 'potato_end', 'potato_f', 'potato_func']

POTATO_BOL = ['TRUE', 'FALSE', 'NULL']                                      # bool, key

POTATO_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']             # num , tol

POTATO_TOL = ['+', '-', '*', '/', '^', '√', ',', '(', ')',                  # num , var, str:+-([.,
              '.', '[', ']', '!', '=', ':', '<', '>']

PLUS, MIN, MUL, DIV, DIV2, POW, SQRT = ['PLUS', 'MINUS', 'MUL', 'DIV', 'FLOAT_DIV', 'POW', 'SQRT']
LB, RB, Q, COMMA, DOT, BR, BL, COLON = ['LB', 'RB', ['\'', '\"'], 'COMMA', 'DOT', 'BR', 'BL', 'COLON']
BE, NOT, LESS, GRE, EQUALS = ['BE', 'NOT', 'LESS', 'GREATER', 'EQUALS']

# - TT - #
TT_POTATO_INT = 'INT'
TT_POTATO_FLT = 'FLOAT'
TT_POTATO_STR = 'STRING'
TT_POTATO_BOL = 'BOOL'
TT_POTATO_POT = 'POTATO'
TT_POTATO_KEY = 'KEYWORD'

N, T, F = None, True, False


class PotatoT:
    def __init__(self, _type__, _value_=None):
        self._type = _type__
        self.value = _value_

    def __repr__(self):
        if not self.value == N:
            return f"{self.value}:{self._type}"
        return self._type
