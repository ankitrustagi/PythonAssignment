class PlayMinion:
	def __init__(self):
		self.vowels = 'a e i o u'.split()

	def _validateString(self, string):
		if not string.isalpha():
			 raise ValueError("Input string must only contain alphabet")
		return string

	def _playGame(self, string, player1, player2):
		player1, player2 = 0, 0
		for index, char in enumerate(string):
			if char.lower() in self.vowels:
				player1 += len(string) - index
			else:
				player2 += len(string) - index
		return player1, player2


if __name__=="__main__":
	game = PlayMinion()
	string = raw_input("Enter Your Word to Play \n")
	game._validateString(string)
	kelvin, Stuart = game._playGame(string, 'Kelvin', '')
	print("Kelvin's score is {}".format(kelvin))
	print("Stuart's score is {}".format(Stuart))
