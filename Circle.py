# Створіть клас Circle зі змінною класу pi, рівною 3.14. Додайте змінну екземпляру radius, 
# ініціалізовану через конструктор. Додайте метод area, який обчислює і повертає площу круга.

class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        if isinstance(radius, (int,float)):
            if radius > 0:
                self.radius = radius
            else:
                raise ValueError("Radius must be more than zero")
        else:
            raise TypeError("Radius must be float or integer only")
    
    def area(self):
        return self.pi*self.radius**2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"


circle = Circle(10)
area = circle.area()

print(circle)
print(f"Area is '{area}'")