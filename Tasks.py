# Задача 1: Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Задача 2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Задача 3: Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

try:
    task = int(input('Введите номер задачи: '))
except ValueError:
    print('Не корректный ввод')
    raise SystemExit
match task:
    case 1:
        try:
            solution = int(input('Задать число отдельно, или использовать pi? (1/2): '))
        except ValueError:
            print('Ввели не верно число')
            raise SystemExit
        match solution:
            case 1:
                number = float(input('Введите число: '))
                d = input('Задайте точность: ')
                value = len(d[2:])
                if value > 10:
                    print('Превышен лимит точности по условию задачи')
                    raise SystemExit 
                elif '-' in d:
                    print('точность не должна быть отрицательной')
                    raise SystemExit
                elif float(d) > 1:
                    print('Не верно задана точность')
                    raise SystemExit
                print(f'%.{value}f' % number)
            case 2:
                import math
                number = math.pi
                d = input('Задайте точность: ')
                value = len(d[2:])
                if value > 10:
                    print('Превышен лимит точности по условию задачи')
                    raise SystemExit 
                elif '-' in d:
                    print('точность не должна быть отрицательной')
                    raise SystemExit
                elif float(d) > 1:
                    print('Не верно задана точность')
                    raise SystemExit
                print(f'%.{value}f' % number)
    case 2:
        try:
            num = int(input('Задайте натуральное число N: '))
        except ValueError:
            print('Не корректный ввод')
            raise SystemExit
        num_list = []
        for n in range(1, num + 1): 
            if num % n == 0:
                num_list.append(n)
        print(num_list)
        result = []
        for i in num_list:
            for ind in range(2, i):
                if i % ind == 0:
                    break
            else:
                result.append(i)
        print(result)
    case 3:
        try:
            solution = int(input('задать список в ручную (1) или использовать готовый(2)?: '))
        except ValueError:
            print('Не корректный ввод')
            SystemExit
        match solution:
            case 1:
                any_list = list(map(int,input('Введит числа через пробел: ').split()))
                print(any_list)
                temp_list= []
                result = []
                for i in any_list:
                    if i not in temp_list:
                        for index in any_list[any_list.index(i) + 1:]:
                            if i == index:
                                break
                        else:
                            result.append(i)
                    temp_list.append(i)
                print(result)
            case 2:
                any_list = [1, 1, 2, 3, 2, 3, 4, 7, 9, 8, 6, 7]
                print(any_list)
                temp_list = []
                result = []
                for i in any_list:
                    if i not in temp_list:
                        for index in any_list[any_list.index(i) + 1:]:
                            if i == index:
                                break
                        else:
                            result.append(i)
                    temp_list.append(i)
                print(result)