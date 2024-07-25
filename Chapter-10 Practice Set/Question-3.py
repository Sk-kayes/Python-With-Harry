class Test():
    a = 69

obj = Test()

print(obj.a) #it print the class attribute because the instance attribute is not set yet.

obj.a = 0 # Instance attribute is set at 0
print(obj.a) # it print the instance attribute because the instance attribute is set.

print(Test.a) # there is no change in the class attribute so it print the class attribute value.