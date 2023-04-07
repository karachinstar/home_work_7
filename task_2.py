# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def count_materials(self, square, height):
        self.mass = int(self._length * self._width * square * height)
        self.height = height
        return f"{self._width}m * {self._length}m * {square}kg * {height}m = {self.mass}kg{' = ' + str(self.mass / 1000) + ' t' if self.mass // 1000 > 0 else ''}"


obj = Road(5000, 20)
print(obj.count_materials(25, 0.05))
