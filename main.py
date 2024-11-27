import math
#Функция Алгоритма Расчет
def Distance(x, y, x1, y1):
    distance = math.sqrt((x1 - x)**2 + (y - y1)**2)
    return print(f"Вычисленное Расстояние между двумя точками на плоскости ({x}, {y}) и ({x1}, {y1}): {distance}")


if __name__ == "__main__":
    x = float(input("Введите точку координаты x0:"))
    y = float(input("Введите точку координаты y0:"))
    x1 = float(input("Введите точку координаты x1:"))
    y1 = float(input("Введите точку координаты y1:"))
    Distance(x_0, y_0, x_1, y_1)
