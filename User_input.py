from ij.gui import GenericDialog
from ij import IJ
import os
import json

def user_input():
	""" Takes user input on experiment parameters and stimulation applications... """
	
	User_Input_List = []
	Stim_List = []
	
	# Takes title, description and number of stims from user.
	gd = GenericDialog("Experiment Parameters:")
	gd.addStringField("Experiment Title:", "ARC-MT/ARC-YP NMDA 12.04.17.01")
	gd.addStringField("Experiment Description:", "")
  	gd.addNumericField("Number of stimulation points:", 1, 1)
  	
  	gd.showDialog()
  	Title = gd.getNextString()
  	Description = gd.getNextString()
  	Nr_Stim = int(gd.getNextNumber())

	User_Input_List.append([Title, Description, Nr_Stim])

	# Creates dialog boxes proportionally to number of stimulations, type and duration. 
  	if Nr_Stim > 1:
  		gd = GenericDialog("Stimulation applications")
  		for stim in range(0, Nr_Stim, 1):
  			gd.addStringField("Stimulation type "+str(stim+1)+":", "NMDA 25 uM")
  			gd.addNumericField("Stimulation start:", stim*2, 2)
  			gd.addNumericField("Stimulation end:", (stim+1)*2, 2)

  	gd.showDialog()

  	# Lists the different stimulations.
	for stim in range(0, Nr_Stim, 1):
		Type_Stim = gd.getNextString()
  		Start_Stim = gd.getNextNumber()
  		End_Stim = gd.getNextNumber()
  		Stim_List.append([Type_Stim, Start_Stim, End_Stim])

	User_Input_List.extend(Stim_List)
	
	# Creates a dictionary of all user inputs.
	User_Input_Dict = {'Parameters': User_Input_List[0]}
	for stim in range(1, Nr_Stim+1, 1):
		User_Input_Dict['Stimulation '+str(stim)] = User_Input_List[stim]

	# Dumps dict to JSON.
	User_Input_Dict = (json.dumps(User_Input_Dict))

	return User_Input_Dict

	
