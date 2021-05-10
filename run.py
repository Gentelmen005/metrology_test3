from indirect_measurement import calculate, init_vars
from sympy.parsing.sympy_parser import parse_expr


def get_essential_data():
    data = {}
    N = int(input("Введите кол-во переменных: "))
    
    print()

    for _ in range(N):
        var = input("Введите название переменной: ")
        data[var] = None

    print()

    for var in data.keys():
        value = float(input(f"Введите значение для переменной {var}: "))
        data[var] = value

    return data


def get_errors(type_: int, data: dict):
    errors = []

    if type_ == 0:
        
        for var in data.keys():
            err = float(input(f"Введите абсолютную погрешность для переменной {var}: "))
            errors.append(err)

    elif type_ == 1:

        for var in data.keys():
            err = float(input(f"Введите систематическую погрешность для переменной {var}: "))
            errors.append(err)

    return errors


def get_standard_deviation(data):
    std_deviation = []

    for var in data.keys():
        std_dev = float(input(f"Введите СКО для переменной {var}: "))
        std_deviation.append(std_dev)

    return std_deviation


def main():
    type_ = int(input("Введите тип задачи: "))
    print()

    data = get_essential_data()
    print()

    errors = get_errors(type_, data)
    print()

    std_deviation = None
    if type_ == 1:
        std_deviation = get_standard_deviation(data)

    print()
    func = input("Введите уравнение: ")
    f = parse_expr(func)

    print()
    coeff = float(input("Введите значение коэффицента доверительной вероятности: "))
    
    print()
    student_coeff = None
    if type_ == 1:
        student_coeff = float(input("Введите значение коэффицента Стьюдента: "))

    vars, subs = init_vars(data)
    calculate(type_, f, errors, coeff, vars, subs, std_deviation, student_coeff)


if __name__ == "__main__":
    main()