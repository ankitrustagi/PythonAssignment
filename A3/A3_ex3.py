import requests

def weatherInfo(place):
	"""
	Find current weather of any city using any weather api.
	"""
	key = "866f5f07f8d96f136ad0efb5a3ee3148"
	URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}".format(place, key)
	try:
		req = requests.get(url = URL)
	except Exception as e:
		return False, "Invalid request"
	# import pdb;pdb.set_trace()
	return True, req.json()


if __name__ == "__main__":
	userPlace = input("Enter Name of the City:		")
	state, info = weatherInfo(userPlace)
	if state:
		currentTemp = info.get("main").get("temp")
		currentTemp = currentTemp - 273.15
		print ("Current temp of {0}, is {1} Degree".format(userPlace, currentTemp))
	else:
		print ("Not a valid city")

