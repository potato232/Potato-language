POTATO_KEY_WORD = ['potato_if ', 'potato_f ', 'potato_break ', 'potato_do',
                   'potato_var ', 'potato_end ', 'potato_loop ', 'potato_func']

POTATO_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']             # num , tol
POTATO_TOL = ['+', '-', '*', '/', '^', '√', ',', '(', ')', '.', '[', ']']   # num , var, str:+-([.,
POTATO_BOL = ['TRUE', 'FALSE', 'NULL']                                      # bool, key

"""

PLUS, MIN, MUL, DIV, POW, SQRT = +  -  *  / //  ^  √
LB, RB, Q, COMMA, DOT, BR, BL  = (  )  '  "  ,  .  [  ]

"""

PLUS, MIN, MUL, DIV, DIV2, POW, SQRT = ['PLUS', 'MINUS', 'MUL', 'DIV', 'FLOAT_DIV', 'POW', 'SQRT']
LB, RB, Q, COMMA, DOT, BR, BL = ['LB', 'RB', ['\'', '\"'], 'COMMA', 'DOT', 'BR', 'BL']

# - TT - #
TT_POTATO_INT = 'INT'
TT_POTATO_FLT = 'FLOAT'
TT_POTATO_STR = 'STRING'
TT_POTATO_BOL = 'BOOL'
TT_POTATO_ARR = 'LIST'

N, T, F = None, True, False


class PotatoT:
    def __init__(self, _type__, _value_=None):
        self._type = _type__
        self.value = _value_

    def __repr__(self):
        if not self.value == N:
            return f"{self.value} : {self._type}"
        return self._type
