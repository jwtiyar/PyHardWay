# Dw class i asayy bo Rectangle w Square
# bo ewey btwanyn em kare kwrtbkyanawa swd le super() werdegryn legell Inheritance (OOP).

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

# Ew dw class ey serewe detwanyn kwrtbkeynewe bem Regeye bykeyn be yek class be swd wergrtn le inheritance w super()
# Super() objecty katyyt bo drwst dekat w enca method eke le superclass werdegret
# Lemey xwarewe superclass brytye le Rectangle w subclass brytye le Square

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length)
        super().__init__(length, length)
# Be hoy super() detwany methody __init__ y rectangle bangbkayt bo bekarthenan le Square subclass.