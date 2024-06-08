# Розробіть клас Vehicle для представлення транспортного засобу. 
# Додайте атрибути, такі як назва, швидкість і вартість. 
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю. 
# Створіть список транспортних засобів і відсортуйте його за швидкістю за допомогою функції sorted()

class Vehicle:
    
    def __init__(self, name, speed, cost):
        self.check_paramaters(name, speed, cost)
        self.name = name
        self.speed = speed
        self.cost = cost
    
    @staticmethod
    def check_paramaters(name, speed, cost):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        if not isinstance(speed, (int,float)):
           raise TypeError("Speed must be an int") 
       
        if speed <= 0:
            raise ValueError("Speed must be more than 0")
        
        if not isinstance(cost,(int,float)):
            raise TypeError("Cost must be an int")
        
        if cost <= 0:
            raise ValueError("Cost must be greather than zero")
        
    
    def __gt__(self, other):
        if not isinstance(other, Vehicle):
            raise NotImplemented
        return self.speed > other.speed
    
    def __str__(self):
        return f"Car with name: '{self.name}' , with speed: '{self.speed}', with cost '{self.cost}'"
    
    def __repr__(self):
        return f"Car('{self.name}', '{self.speed}', '{self.cost}'"



v2 = Vehicle("Name2", 110, 9000)
v1 = Vehicle("Name1", 150, 10000)
result = sorted([v1, v2])
print(result)
print(v1 > v2)