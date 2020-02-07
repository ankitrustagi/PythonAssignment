#A special quidditch match is being organised at Hogwarts where all four houses play together. 
# All the audience is seated in a single row. Each person in the audience has a favorite team and they are seated 
# in a manner that they are scattered all over the row in multiple small groups. You are tasked with handing
#  over the team placard to each person in the audience as per their individual favorite team. 
# You are prohibited from carrying placards of any two teams together, i.e, you can carry the placards of a 
# single team at one time, but there is no restriction on the number of placards you can carry. So being an 
# effective organiser, you come up with a plan to carry placards in group. See below for a representation.
# (Gryffindor > G, Slytherin > S, HufflePuff > H, Ravenclaw > R)

def countHouseCard(cards):
	lastCard = ''
	result = []
	for card in cards:
		if card == lastCard:
			result[-1] = (card, result[-1][1] +1)
		else:
			result.append((card, 1))
			lastCard = card
	return result

if __name__=="__main__":
	seatingOrder = input("Enter Audience Seating Order")
	if str(seatingOrder):
		print (countHouseCard(seatingOrder))
	else:
		print("Enter a valid input")
