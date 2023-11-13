while True:
    try:
        print('введите длину первого катета')
        a=int(input())
        print('введите длину второго катета')
        b=int(input())
        s=a*b*0.5
        import math
        p=a+b+math.sqrt(a**2+b**2)
        print(f"площадь:{s:.2f}, периметр: {p:.2f} ")
    except ValueError as e:
        print(f"Value Erroe {e}")
        continue
    except Exception as e:
        print(f"Unrecognized exception {e}")
        continue
    break