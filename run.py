from indirect_measurement import calculate, init_vars
from sympy.parsing.sympy_parser import parse_expr


def main():
    data = {}
    absolute_errors = []

    N = int(input("Введите кол-во переменных: "))
    
    print('\n')

    for _ in range(N):
        var = input("Введите название переменной: ")
        data[var] = None

    print('\n')

    for var in data.keys():
        value = float(input(f"Введите значение для переменной {var}: "))
        data[var] = value

    print('\n')

    for var in data.keys():
        err = float(input(f"Введите абсолютное погрешность для переменной {var}: "))
        absolute_errors.append(err)

    print('\n')

    v, subs = init_vars(data)
    func = input("Введите уравнение: ")
    f = parse_expr(func)

    print('\n')

    student_coeff = float(input("Введите значение коэффицента доверительной вероятности: "))

    print('\n')

    calculate(f, absolute_errors, student_coeff, v, subs)


if __name__ == "__main__":
    main()