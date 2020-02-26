class MyClass:
    i = 12345
    def f(self):
        return "hello world"

myclass = MyClass()  
print (myclass.f())

class Complex:
    def __init__(self,realpart,imagpart):
        self.i = realpart
        self.j = imagpart
x = Complex(3.0,-4.5)
# print(x.i)