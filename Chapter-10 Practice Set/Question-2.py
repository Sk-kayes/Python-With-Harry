# Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class Calculator:

    def __init__(self, a):
        self.a = a

    def square(self):
        print(f"The Square of {self.a} is {self.a * self.a}")

    def cube(self):
        print(f"The Cube of {self.a} is {self.a * self.a * self.a}")

    def sqrt(self):
        print(f"The Square root of {self.a} is {self.a ** (1/2)}")

sq = Calculator(5)
sq.square()
sq = Calculator(4)
sq.cube()
sq = Calculator(16)
sq.sqrt()