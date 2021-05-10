from sympy import symbols, diff
from math import sqrt


def init_vars(data: dict):
    v = { v.name: v for v in symbols(list(data.keys())) } 
    subs = { v[key]: data[key] for key in v.keys() }

    return v, subs


def calculate(type_, func, errors, coeff, vars: dict, subs: dict, std_deviation, student_coeff):
    f = func.evalf(subs=subs)
    print(f"Считаем исходное выражение: {func} = {f}")

    print("\nСчитаем производные:")
    func_diffs = calculate_diffs(func, vars, subs)
    
    result = [(func_diffs[i] * errors[i]) ** 2 for i in range(len(func_diffs))]
    err = coeff * sqrt(sum(result))

    if type_ == 0:
        print(f"\nОбщая погрешность: {err}")
        print(f"\nРезультат: {f} +- {err}")

    elif type_ == 1:
        print(f"\nСуммарная систематическая погрешность: {err}")

        sE = sqrt(sum([(func_diffs[i] * std_deviation[i]) ** 2 for i in range(len(func_diffs))]))
        print(f"\nsE = {sE}")

        s0 = sqrt(1 / 3 * sum([(func_diffs[i] * errors[i]) ** 2 for i in range(len(func_diffs))]))
        print(f"\ns0 = {s0}")

        eE = student_coeff * sE
        print(f"\nСуммарная случайная погрешность, eE = {eE}")

        sGen = sqrt(sE ** 2 + s0 ** 2)
        print(f"\nS общ = {sGen}")

        Ke = (eE + err) / (sE + s0)
        print(f"\nКе = {Ke}")

        total_err = Ke * sGen
        print(f"\nОбщая погрешность = {total_err}")

        print(f"\nРезультат = {f} +- {total_err}")

        


def calculate_diffs(func, vars, subs):
    result = []
    
    for v in vars:
        f = diff(func, vars[v])
        result.append(f.evalf(subs=subs))
        print(f"dF/d{v} = {f} = {result[-1]}")

    return result