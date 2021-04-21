from Capteur import Captor 
class QTable :

	def __init__ (self) :
		self.qTable = [[0, 0], [0, 0], [0, 0], [0, 0]] # Index qTable [] : 0 : Not Jump & 1 : Jump
		self.stateIndex = {
			(Captor.ERROR, Captor.ERROR): -1,
			(Captor.LIGHT, Captor.LIGHT): 0,
			(Captor.LIGHT, Captor.DARK) : 1,
			(Captor.DARK, Captor.LIGHT) : 2,
			(Captor.DARK, Captor.DARK)  : 3
		}

	def getStateValue (self, c1, c2) :
		return self.stateIndex [(c1, c2)]

	def predict (self, state) :
		return self.qTable [state].index (max (self.qTable [state]))

	def getMaxValue (self, state) :
		return max (self.qTable [state])

	def setValue (self, state, actionPerformed, newValue) :
		self.qTable [state] [actionPerformed] = newValue

	def getValue (self, state, action) :
		return self.qTable [state] [action]

	def getTable (self) :
		return self.qTable
