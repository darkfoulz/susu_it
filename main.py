import math

def Distance(x_0, y_0, x_1, y_1):
    distance = math.sqrt((x_1 - x_0)**2 + (y_0 - y_1)**2)
    return print(f"Расстояние между двумя точками ({x_0}, {y_0}) и ({x_1}, {y_0}): {distance}")


if __name__ == "__main__":
    x_0 = int(input("Введите точку координаты x0:"))
    y_0 = int(input("Введите точку координаты y0:"))
    x_1 = int(input("Введите точку координаты x1:"))
    y_1 = int(input("Введите точку координаты y1:"))
    Distance(x_0, y_0, x_1, y_1)
