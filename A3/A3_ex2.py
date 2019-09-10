"""
You are given a valid JSON document, and you have to print its score. 
The score is calculated by the sum of the scores of each element. 
For any element, the score is equal to the number of attributes it has.
"""
import json
count = 0
def id_generator(dict_var):
	global count
	for k, v in dict_var.items():
		if isinstance(v, dict):
			id_generator(v)
		elif isinstance(v, list):
			for key in v:
				if isinstance(key, dict):
					id_generator(key)
				else:
					count = count + 1
		else:
			count = count + 1

if __name__=="__main__":
	with open('test.json') as json_file:
		data = json.load(json_file)
		id_generator(data)
		print count



