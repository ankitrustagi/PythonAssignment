from itertools import combinations

def findProbability(inputLen, inputList, inputCombinationLength):
	inputCombination = list(combinations(range(1, inputLen + 1), inputCombinationLength))
	selectedList = list()
	for index,char in enumerate(inputList):
		if char.lower() == 'a':
			selectedList.append(index+1) 

	value = float(len(set([comb for selected in selectedList for comb in inputCombination if selected in comb])))/len(inputCombination)
	print value

if __name__=="__main__":
	inputLen = int(raw_input("Enter the length of Input \n"))
	inputList = raw_input("Enter input character's with space \n").split()
	inputCombinationLength = int(raw_input("Enter number of indices to be selected \n"))
	findProbability(inputLen, inputList, inputCombinationLength)






