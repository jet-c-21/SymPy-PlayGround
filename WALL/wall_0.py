# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2022/3/4
"""
import sympy as sp
from pprint import pp

x = sp.Symbol('x')
eq2 = sp.Eq(sp.cos(x) - sp.sin(x), 0)
print(type(eq2))
pp(dir(eq2))
