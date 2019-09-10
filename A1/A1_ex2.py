"""
Remove Duplicate Item From The List.
"""
"""
Write a program to remove duplicate elements from a user given list.
"""
def remove_duplicate(lst):
	return list(set(lst))

if __name__ == "__main__":
	lst = [1,2,3,3,4,5,1]
	lst = ['ankit', 'rustagi', 1,2,3,1,'rustagi']
	print("Actual List:		")
	print(lst)
	newlst = remove_duplicate(lst)
	print ("New List:	")
	print (newlst)