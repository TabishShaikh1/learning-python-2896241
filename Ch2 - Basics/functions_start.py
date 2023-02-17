#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a Function")

# TODO: function that takes arguments
def Func2(arg1, arg2):
    print(arg1," ",arg2)

# TODO: function that returns a value
def cube(x):
    return x * x * x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result= result * num
    return result    

# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result= result + x
    return result    




func1()
print(func1())
print(func1)

Func2(10,20)
print(Func2(10,20))
print(cube(5))

print(power(4))
print(power(3,2))

print(multi_add(3,4,25,6,2))