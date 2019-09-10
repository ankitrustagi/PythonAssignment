"""
Create a game in which the user is presented with an anagram of a word and has to guess the right word within a limited number of attempts.
"""
import random

anagramDict = {
	"abler" : ['baler', 'blare', 'blear'],
	"bedares": ['debaser', 'rebased', 'sabered'],
	"deils": ['idles', 'sidle', 'slide'],
	"evil": ['live', 'veil', 'vile'],
	"outskate": ['outtakes', 'stakeout', 'takeouts'],
	"overtips": ['pivoters', 'repivots', 'sportive'],
	"delivers": ['desilver', 'silvered', 'slivered']}

if __name__ == "__main__":
	listOfAnagramWords = ['abler', 'bedares', 'deils', 'evil', 'outskate', 'overtips', 'delivers']
	anagramWord = random.choice(listOfAnagramWords)
	attempts = 3
	print("Please type anagram of the word..{0}" .format(anagramWord))
	print("Type a correct anagram within {0} attempts".format(attempts))
	while attempts:
		userChoice = input("Please type your word :		")
		if userChoice in anagramDict.get(anagramWord):
			print ("Yes!! it's a right anagram, Thank You")
			break
		else:
			print ("Wrong anagram !!!")
		attempts -= 1




