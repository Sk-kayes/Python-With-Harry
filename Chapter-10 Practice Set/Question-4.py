# Add a static method in problem 2, to greet the user with hello.

class Calculator:

    def __init__(self, a):
        self.a = a

    def square(self):
        print(f"The Square of {self.a} is {self.a * self.a}")

    def cube(self):
        print(f"The Cube of {self.a} is {self.a * self.a * self.a}")

    def sqrt(self):
        print(f"The Square root of {self.a} is {self.a ** (1/2)}")

    @staticmethod
    def greet():
        print("Hello")

sq = Calculator(5)
sq.greet()
sq.square()
sq = Calculator(4)
sq.cube()
sq = Calculator(16)
sq.sqrt()