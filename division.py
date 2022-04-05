print("Only division of Two numbers can be performed")
def div(x,y):                       #the use of function is to simplify the task for longer code
    return x/y
    
x = float(input("Enter the first number: "))  #here we are taking the input from user 
y = float(input("Enter the second number: "))    #here also we are taking input from user
# using basic if condition to let the user know that y = 0 is not defined and code will produce a error... 
if y == 0:
    print("y=0, is not defined. Therefore an error would occur")

print("The division of " + str(x) + " and " + str(y) + " is " + str(div(x,y)))