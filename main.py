import math
#Функция Алгоритма Расчет
def Distance(x0, y0, x1, y1):
    distance = math.sqrt((x1 - x0)**2 + (y0 - y1)**2)
    return print(f"Расстояние между двумя точками ({x0}, {y0}) и ({x1}, {y0}): {distance}")


if __name__ == "__main__":
    x0 = float(input("Введите точку координаты x0:"))
    y0 = float(input("Введите точку координаты y0:"))
    x1 = float(input("Введите точку координаты x1:"))
    y1 = float(input("Введите точку координаты y1:"))
    Distance(x_0, y_0, x_1, y_1)
