import math

def Distance(x_0, y_0, x_1, y_1):
    distance = math.sqrt((x_1 - x_0)**2 + (y_0 - y_1)**2)
    return print(f"Расстояние между двух точек {distance}")

if __name__ == "__main__":
    x_0 = float(input("Введите точку координаты x0:"))
    y_0 = float(input("Введите точку координаты y0:"))
    x_1 = float(input("Введите точку координаты x1:"))
    y_1 = float(input("Введите точку координаты y1:"))
    Distance(x_0, y_0, x_1, y_1)