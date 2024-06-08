# Створіть клас Rectangle для представлення прямокутника. 
# Додайте методи для обчислення площі та периметра прямокутника. 
# Створіть об'єкт Rectangle і викличте ці методи.

# Приклад використання:
# rect = Rectangle(2, 4)
# square = rect.square()
# perimeter = rect.perimeter()

class Rectangle:
    
    def __init__(self, width, height):
        if isinstance(width, (int,float)) and isinstance(height, (int,float)):
            if width > 0 and height > 0:
                self.width = width
                self.height = height
            else:
                raise ValueError("Width and Height must be more than zero")
        else:
            raise TypeError("Width and Height must be integers")
        
    def square(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
    def __str__(self):
        return f"Rectangle with width: '{self.width}' and height: '{self.height}'"


rect = Rectangle(2,1)
square = rect.square()
perimeter = rect.perimeter()
print(rect)
print(f"Square of rect is {square}")
print(f"Perimeter of rect is {perimeter}")