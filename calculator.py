while True:
    try:
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
        c = float(input("Введите значение c: "))
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            print("\n", x1, "\n", x2)
        elif d == 0:
            x = (-b) / (2 * a)
            print(x)
        elif d < 0:
            print("нет корней")

    except ValueError:
        print("это не число")
        continue