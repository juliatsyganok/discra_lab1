from task1 import in_span
from task2 import bas
from task3 import change_center
from task4 import limit_infty
from part1.class_polynom import Polynom

while True:
    print("Номер задачи или exit: ")
    ch = input().lower()
    if ch == "exit":
        break
    elif ch == "1":
        print("Введите коэффициенты полинома f (от младшего к старшему): ")
        f = Polynom(list(map(float, input().split())))
        print("Введите количество полиномов в множестве G: ")
        n = int(input())
        gs = []
        for i in range(n):
            print(f"Введите коэффициенты полинома g{i+1} (от младшего к старшему): ")
            gs.append(Polynom(list(map(float, input().split()))))
        res, coeffs = in_span(f, gs)
        if res:
            print("f принадлежит . Коэффициенты: ", coeffs)
        else:
            print("f не принадлежит")

    elif ch == "2":
        print("Введите коэффициенты полинома f (от младшего к старшему): ")
        f = Polynom(list(map(float, input().split())))
        print("Введите точку a: ")
        a = float(input())
        print("Коэффициенты разложения: ", bas(f, a))
    elif ch == "3":
        print("Введите коэффициенты полинома (от младшего к старшему): ")
        coeffs = list(map(float, input().split()))
        print("Введите a: ")
        a = float(input())
        print("Введите B: ")
        B = float(input())
        print("Коэффициенты: ", change_center(coeffs, a, B))
    elif ch == "4":
        print("Введите коэффициенты полинома f (от младшего к старшему): ")
        f = Polynom(list(map(float, input().split())))
        print("Введите коэффициенты полинома g (от младшего к старшему): ")
        g = Polynom(list(map(float, input().split())))
        print("Предел: ", limit_infty(f, g))