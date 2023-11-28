
POTATO_KEY_WORD = ['potato_if', 'potato_push',
                   'potato_var', 'potato_func',
                   'potato_loop', 'potato_b',
                   'potato_f', 'potato_v']

POTATO_BOL = ['TRUE', 'FALSE', 'NULL']                                      # bool, key

POTATO_NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']             # num , tol

POTATO_TOL = ['+', '-', '*', '/', '^', '√', ',', '(', ')',                  # num , var, str:+-([.,
              '.', '[', ']', '!', '=', ':', '<', '>', '{', '}']

PLUS, MIN, MUL, DIV, DIV2, POW, SQRT = ['PLUS', 'MINUS', 'MUL', 'DIV', 'FLOAT_DIV', 'POW', 'SQRT']
LB, RB, Q, COMMA, DOT, BR, BL, COLON = ['LB', 'RB', ['\'', '\"'], 'COMMA', 'DOT', 'BR', 'BL', 'COLON']
BE, NOT, LESS, GRE, EQUAL, DO, END = ['BE', 'NOT', 'LESS', 'GREATER', 'EQUALS', 'DO', 'END']

# - TT - #
TT_POTATO_INT = 'INT'
TT_POTATO_FLT = 'FLOAT'
TT_POTATO_STR = 'STRING'
TT_POTATO_BOL = 'BOOL'
TT_POTATO_POT = 'VAR'
TT_POTATO_KEY = 'KEYWORD'

N, T, F = None, True, False


class PotatoT:
    def __init__(self, _type__, _value_=None):
        self._type = _type__
        self.value = _value_

    def __repr__(self):
        if not self.value == N:
            return f'{self._type}:{self.value}'
        return self._type


class PotatoV:
    def __init__(self, _value_):
        self._value_ = _value_
        self._variable_ = {}

    def __repr__(self):
        return self._value_

    def get(self, x):
        if x in self._variable_:
            return self._variable_[x]
        return N


class PotatoK:
    def __init__(self, _value_):
        self._value_ = _value_

    def __repr__(self):
        return self._value_


class PotatoF:
    def __init__(self, _value_):
        self._value_ = _value_
        self._func__ = {}

    def __repr__(self):
        return self._value_

    def get(self, x):
        if x in self._func__:
            return self.run(self._func__[x])
        return N

    def run(self, f):
        pass
