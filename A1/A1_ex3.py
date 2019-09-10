"""
Remove string from list and return square of list item
"""
def checkSquare(element):
	if type(element) is int:
		return element*element

finalList = []
if __name__ == "__main__":
	#lst = [1,2,3,3,4,5,1]
	lst = ['ankit', 'rustagi', 1,2,3,1,'rustagi']
	result = map(checkSquare, lst)
	result =[value for value in list(result) if value != None]
	print("Result of square list is:	"result)