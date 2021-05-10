> **WARNING**: Прога не считает абсолютные погрешности, значение коэффицента дов. вероятности и значение коэффицента Стьюдента!

# Пример для решения из практики

## Пример 1
[Практика 6 гр. 438-1, 7 минута 7 секунда](https://skynet.2i.tusur.ru/playback/presentation/2.0/playback.html?meetingId=63609490961c34944bce2ccff61cef4fa2a3d0ec-1619494504161&t=7m7s)

```shell
$ python run.py
Введите тип задачи: 0

Введите кол-во переменных: 5

Введите название переменной: i
Введите название переменной: r1
Введите название переменной: r2
Введите название переменной: r3
Введите название переменной: u0

Введите значение для переменной i: 0.009
Введите значение для переменной r1: 100
Введите значение для переменной r2: 51
Введите значение для переменной r3: 2.4
Введите значение для переменной u0: 2

Введите абсолютную погрешность для переменной i: 0.000135
Введите абсолютную погрешность для переменной r1: 1
Введите абсолютную погрешность для переменной r2: 0.5
Введите абсолютную погрешность для переменной r3: 0.024
Введите абсолютную погрешность для переменной u0: 0.03


Введите уравнение: i * (r1 - r2) ** 2 / r3 - u0

Введите значение коэффицента доверительной вероятности: 1.1 

Считаем исходное выражение: i*(r1 - r2)**2/r3 - u0 = 7.00375000000000

Считаем производные:
dF/di = (r1 - r2)**2/r3 = 1000.41666666667
dF/dr1 = i*(2*r1 - 2*r2)/r3 = 0.367500000000000
dF/dr2 = i*(-2*r1 + 2*r2)/r3 = -0.367500000000000
dF/dr3 = -i*(r1 - r2)**2/r3**2 = -3.75156250000000
dF/du0 = -1 = -1.00000000000000

Общая погрешность: 0.48707430442395355

Результат: 7.00375000000000 +- 0.48707430442395355
```

## Пример 2
[Практика 6 гр. 438-1, 43 минута 45 секунда](https://skynet.2i.tusur.ru/playback/presentation/2.0/playback.html?meetingId=63609490961c34944bce2ccff61cef4fa2a3d0ec-1619494504161&t=43m45s)

```shell
$ python run.py
Введите кол-во переменных: 2

Введите название переменной: c1
Введите название переменной: c2

Введите значение для переменной c1: 94.8
Введите значение для переменной c2: 102.3

Введите систематическую погрешность для переменной c1: 0.9
Введите систематическую погрешность для переменной c2: 1.1

Введите СКО для переменной c1: 0.5
Введите СКО для переменной c2: 0.5

Введите уравнение: c2 - c1

Введите значение коэффицента доверительной вероятности: 1.1

Введите значение коэффицента Стьюдента: 1.96
Считаем исходное выражение: -c1 + c2 = 7.50000000000000  

Считаем производные:
dF/dc1 = -1 = -1.00000000000000
dF/dc2 = 1 = 1.00000000000000

Суммарная систематическая погрешность: 1.5633937443907089

sE = 0.7071067811865476

s0 = 0.8205689083394114

Суммарная случайная погрешность, eE = 1.3859292911256331 

S общ = 1.0832051206181281

Ке = 1.930594991945917

Общая погрешность = 2.091230381115531

Результат = 7.50000000000000 +- 2.091230381115531
```