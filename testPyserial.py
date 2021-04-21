from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
import serial
import sys
import time
import Game
import _thread
import Capteur
import QTable
import random
import time

from datetime import datetime

#browser = webdriver.Chrome ()
#browser.get ("https://translate.google.com/?hl=fr")

port = serial.Serial('COM3', 9600)
game = Game.Game ()
game.press_up ()

INITIAL_EPSILON = 0.1
ALPHA = 0.5
FINAL_EPSILON = 0.0001
GAMMA = 0.99

choosen_action = -1
observation = 0
reward = 0
updateQValue = 0
qtable = QTable.QTable ()
current_state = -1
next_state = -1
epsilon = INITIAL_EPSILON
file = open ("QTableSaves.txt", "w")

def getValue (obs) : # \r \n
	line = port.readline ().decode ("utf-8")
	value = -1
#	print (line)
	if len (line) <= 2 :
		return (Capteur.Captor.ERROR, Capteur.Captor.ERROR)

	if line.find ("\r") != -1 :
		line = line.split ("\r") [0]

	return Capteur.getValueFromAnalog (line, obs)

"""
Reward :
	- If not crashed, reward = 0.1
	- If crashed, reward = -1
"""

while (True) :

	if observation % 1000 == 0 and epsilon > FINAL_EPSILON :
		epsilon -= 0.0001


	elif game.get_crashed () :
		port.close ()
		port.open ()
		time.sleep (1)
		game.press_up ()
	#	current_state = qtable.getStateValue (*getValue ())

	#else :
	#	current_state = next_state
	current_state = qtable.getStateValue (*getValue (observation)) # observe, get state

# Choose an action
	if random.random () < epsilon :
		choosen_action = random.randint (0, 1)
	else :
		choosen_action = qtable.predict (current_state)

# Act
	if choosen_action == 1 :
		game.press_up ()
	else :
		pass

# Observe, get reward and next state
	if game.get_crashed () :
		reward = -1
	else :
		reward = 0.1

	next_state = qtable.getStateValue (*getValue (observation))

# Update
	qtable.setValue (current_state, choosen_action, (1 - ALPHA ) * qtable.getValue (current_state, choosen_action) + ALPHA * (reward + GAMMA * qtable.getMaxValue (next_state)))

# update time
	observation = observation + 1

	if current_state != 0 :
		print ("TimeStep:{}|Action:{}|State:{}|Score:{}|Epsilon:{}".format (observation, choosen_action, current_state, game.get_score (), epsilon))

# save q table each 1000 observation
	if observation % 1000 == 0 :
		for state in qtable.getTable () :
			line = ""
			for action in state :
				line += "{},".format (str (action))

			file.write (line)

			file.write ("\n")
		file.write ("\n")

		if epsilon > FINAL_EPSILON :
			epsilon -= 0.0001

