#1. Импортируем модуль numpy, дадим ему имя np

import numpy as np
#2. Сформируем массивы координат движения снаряда:

x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])

h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 
 447.8, 434.1, 441.4])
#3. Построим траекторию движения снаряда, используя в качестве линии тренда полином второй степени. Найдем его коэффициенты:

a = np.polyfit(x_array, h_array, 2)
#4. Создадим функцию для вычисления значений полинома второй степени в точке x, разместим ее в начале программы, после импорта модуля:

def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
#5. С помощью полученного тренда вычислим высоту, на которой находилась пушка. Значение координаты по оси ОХ в этой точке равно 0.

h_zero = get_trend(0, a)

print("Высота, на которой стоит пушка: %6.2f м" % h_zero)
#6. Вычислим, на какой высоте будет находиться снаряд в точке по оси ОХ, где расположена мишень

x_target = 1450

h_target = get_trend(x_target, a)

print("Высота, в точке %4d м: %6.2f м" % (x_target, h_target))
#7. Определим, попадет ли снаряд в цель, если известно что мишень расположена на высоте 51 метр, учитывая, что радиус мишени 50 см =0.5 м. Для этого найдем модуль разности между высотой, на которой расположена мишень, и положением снаряда, вычисленного с помощью линии тренда. Затем сравним полученное значение с радиусом мишени и выведем результат.

delta_h = abs(51 - h_target)

if delta_h <= 0.5:

    print("Снаряд попадет в мишень.")

else:

    print("Снаряд не попадет в мишень.")