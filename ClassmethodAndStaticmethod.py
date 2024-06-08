# До класу Circle створеного у попередньому завданні додайте два метода, 
# класметод from_diameter, який буде приймати діаметр та 
# повертати екземпляр класу з радіусом розрахованим з переданого у метод діаметру. 
# Додайте статикметод check_radius, який буде отримувати радіус, 
# та перевіряти його на валідність (радіус повинен бути більший за 0)

class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        self.check_radius(radius)
        self.radius = radius

    def area(self):
        return self.pi*self.radius**2
    
    @classmethod
    def from_diameter(cls, diamater):
        radius = diamater / 2
        return cls(radius)
    
    @staticmethod
    def check_radius(radius):
       if not isinstance(radius, (int,float)):
            raise TypeError("Radius must be float or integer only")
       elif radius <= 0:
            raise ValueError("Radius must be more than zero")
    
    def __str__(self):
        return f"Circle with radius {self.radius}"



circle = Circle.from_diameter(10)
area = circle.area()
Circle.check_radius(17)

print(circle)
print("Area is {area}")
