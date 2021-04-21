from enum import Enum

class Captor (Enum) :
	LIGHT = 1
	DARK = 2
	ERROR = 3

def getValueFromAnalog (valuesStr, obs) :

	c1Value = Captor.ERROR
	c2Value = Captor.ERROR

	values = valuesStr.split ("|")

	try :
		int (values [0])
		int (values [1])
	except :
		return (c1Value, c2Value)

	if int (values [0]) >= 70 :
		c1Value = Captor.LIGHT
	if int (values [0]) < 70 :
		c1Value = Captor.DARK

	if int (values [1]) >= 40 :
		c2Value = Captor.LIGHT
	if int (values [1]) < 40 :
		c2Value = Captor.DARK

	if c1Value == Captor.DARK or c2Value == Captor.DARK :
		print ("T:{}|C1:{}|C2:{} | {}".format (obs, c1Value.name, c2Value.name, valuesStr))

	return (c1Value, c2Value)