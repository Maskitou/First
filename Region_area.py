#https://younglinux.info/oopython/operators.php
#https://pythonworld.ru/osnovy/peregruzka-operatorov.html
import math

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)
    def __str__(self):
        return f"Circle(r={self.r})"
class Rect:
    def __init__(self, length, width):
        self.length = length
        self. width = width
    def area(self):
        return self.width * self.length
    def __str__(self):
        return f'Rect = {self.length},{self.width}'
class Triangle:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third
    def area(self):
        p = (self.first + self.second + self.third)/2
        return math.sqrt(p*(p-self.first)*(p - self.second)*(p - self.third))
    def __call__(self, *args, **kwargs): # это я учусь новым маг. методам
        print(args,'kwargs:',kwargs)
        return 'К объекту обратились как к функции'
    def __str__(self):
        return f'Triangle = {self.first},{self.second},{self.third}'
def is_digit(string):
    if string.isdigit():
       return string
    else:
        try:
            string = float(string)
            return string
        except ValueError:
            return False
with open(r'C:\Users\Max\Desktop\Programm Clondike\Проекты\figures.txt') as file: # ПРОВЕРКА НА ЧИСЛО
    s_list = []
    for line in file:
        a = line.split(',')
        a = [line.rstrip() for line in a]
        b = []
        for i in a:
            if i.isalpha():
                pass
            else:
                b.append(float(is_digit(i)))
        if a[0] == "Triangle":
            s = Triangle(b[0],b[1],b[2]).area()
            s_list.append(s)
        elif a[0] == 'Rect':
            s = Rect(b[0],b[1]).area()
            s_list.append(s)
        elif a[0] == 'Circle':
            s = Circle(b[0]).area()
            s_list.append(s)
        print(s)
while len(s_list) > 5:
    s_list.remove(min(s_list))
print("Топ 5 больших фигур:",s_list)
