from sympy import symbols, diff
from math import sqrt


def init_vars(data: dict):
    v = { v.name: v for v in symbols(list(data.keys())) } 
    subs = { v[key]: data[key] for key in v.keys() }

    return v, subs


def calculate(func, absolute_errors, student_coeff, vars: dict, subs: dict):
    f = func.evalf(subs=subs)
    print("Считаем исходное выражение: {0} = {1}".format(func, f))

    print("\nСчитаем производные:")
    func_diffs = calculate_diffs(func, vars, subs)
    
    result = [(func_diffs[i] * absolute_errors[i]) ** 2 for i in range(len(func_diffs))]

    total_err = student_coeff * sqrt(sum(result))
    print("\nОбщая погрешность: {0}".format(total_err))

    print("\nРезультат: {0} +- {1}".format(f, total_err))


def calculate_diffs(func, vars, subs):
    result = []
    
    for v in vars:
        f = diff(func, vars[v])
        result.append(f.evalf(subs=subs))
        print("dF/d{0} = {1} = {2}".format(v, f, result[-1]))

    return result