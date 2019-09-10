# Python Program to Reverse a Number using While loop    

def reverseNum(number):
	Reverse = 0    
	while(Number > 0):    
		Reminder = Number %10    
		Reverse = (Reverse *10) + Reminder    
		Number = Number //10    
		print("\n Reverse of entered number is = %d" %Reverse)


if __name__=="__main__":
	try:
		Number = int(input("Please Enter any Number: "))
		reverseNum(Number)
	except:
		print("Enter a valid number")
