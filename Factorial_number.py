if __name__ == '__main__':
    def factorial(x):
        """This is a recursive function
        to find the factorial of an integer"""

        if x == 1:
            return 1
        else:
            return x * factorial(x - 1)
    num = 5
    print("The factorial of", num, "is", factorial(num))
    
#Import math Library
#import math

#Return factorial of a number
#print(math.factorial(9))
#print(math.factorial(6))
#print(math.factorial(5))