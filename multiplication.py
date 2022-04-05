print("Only multiplication of Two numbers can be performed")
def mul(x,y):                       #the use of function is to simplify the task for longer code
    return x*y
    
x = float(input("Enter the first number: "))  #here we are taking the input from user 
y = float(input("Enter the second number: "))    #here also we are taking input from user

print("The product of " + str(x) + " and " + str(y) + " is " + str(mul(x,y)))