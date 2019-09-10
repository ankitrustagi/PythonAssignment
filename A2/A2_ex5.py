"""
Write a programme to find out whether given string is a valid regex or not.
"""
import re

def validateString(my_reg):
	try:
		re.compile(my_reg)
		return True
	except:
		return False

if __name__ == "__main__":
	my_ex = input("Please Enter Your Regular Expression:	")
	is_valid_re = validateString(my_ex)
	if is_valid_re:
		print ("Its a valid regular expression.")
	else:
		print ("!!! Please try again.")