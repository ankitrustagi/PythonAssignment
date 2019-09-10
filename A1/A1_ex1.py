# Function for nth Fibonacci number 
def fibonacci(n): 
    """
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

    """
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        print(a) 
    elif n == 1: 
        print(b)
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
            print (b) 

if __name__ == "__main__":
    num = input("Enter Number:  ")
    try:
        fibonacci(int(num))
    except:
        print("Enter a valid number")

