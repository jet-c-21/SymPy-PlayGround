# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/4
"""
import sympy as sp
from pprint import pp

sp.init_printing(use_unicode=True)

x = sp.Symbol('x')
expr = x ** 2
print(expr)
eq2 = sp.Eq(sp.cos(x) - sp.sin(x), 0)
print(eq2)
# print(type(eq2))
# pp(dir(eq2))

sp.Limit
