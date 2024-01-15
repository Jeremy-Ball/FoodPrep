import sys
from unittest import mock
from foodprep import *

class BoundaryAnalysis():
	
	def __init__(self):
		self.self = self
	
	def item_Boundary(self):
				#define input values and expected print statements then put them in lists
	
		stateList = [] #values to mock
		printList = [] #statment to assert
		
		#this is where the program should begin reading assertions. Set to begin where print statements begin occuring
		listPosition = 0
		
		state1 =("1234567891234567")
		print1 =  ("Item may not be more than 15 characters")
		state2 = ""
		print2 = ("Invalid input")
		
		state3 = "Onion()"
		print3 = ("Special characters not allowed")
		
		state4 = "-<>Onion"
		print4 = ("Special characters not allowed")
		
		stateList.append(state1)
		stateList.append(state2)
		stateList.append(state3)
		stateList.append(state4)
		printList.append(print1)
		printList.append(print2)
		printList.append(print3)
		printList.append(print4)

		with mock.patch("builtins.input", side_effect = stateList):
			original = sys.stdout #Original  data stream	
				#captures all print statements and writes them to the filled called 'redirect'
			sys.stdout = open('redirect.txt', 'w') 
				
			try: #checks for StopIteration error
				FoodPrep(itemList = []).validateItem() #method to test
			except StopIteration:
				#Return original values to sys.stdout and closes the file
				sys.stdout = original 
		
		#creates headers for the test			
		print("Test Input                 Expected output")
		print("")
					
		with open("redirect.txt", "r") as testText:
			line = testText.read() #reads file
			line = line.split("\n")	#creates a list
			line = [i for i in line if i] #removes empty elements
			
			#print(line) #!!! use this to discover listPosition !!!
	
			i = 0 #variable to start loop
			while i != 4:
				try: 
					assert line[listPosition] == printList[i] #assertions
					print(stateList[i].ljust(16) + " ------->      " + line[listPosition] + "\n")
					i += 1
					listPosition += 1
				except AssertionError:
					print("     ERROR  " + stateList[i] + " != " + line[listPosition] + "\n")
					i += 1
					listPosition += 1

#-----------------------------------------

	def cost_Boundary(self):
				#define input values and expected print statements then put them in lists
	
		stateList = [] #values to mock
		printList = [] #statment to assert
		
		#this is where the program should begin reading assertions. Set to begin where print statements begin occuring
		listPosition = 0
		
		state1 =("12345678")
		print1 =  ("Length of cost is too long")
		
		state2 = ""
		print2 = ("Cost needs to be numbers only")
		
		state3 = "Onion()"
		print3 = ("Cost needs to be numbers only")
		
		state4 = "-<>Onion"
		print4 = ("Cost needs to be numbers only")
		
		stateList.append(state1)
		stateList.append(state2)
		stateList.append(state3)
		stateList.append(state4)
		printList.append(print1)
		printList.append(print2)
		printList.append(print3)
		printList.append(print4)

		with mock.patch("builtins.input", side_effect = stateList):
			original = sys.stdout #Original  data stream	
				#captures all print statements and writes them to the filled called 'redirect'
			sys.stdout = open('redirect.txt', 'w') 
				
			try: #checks for StopIteration error
				FoodPrep(itemList = []).validateCost() #method to test
			except StopIteration:
				#Return original values to sys.stdout and closes the file
				sys.stdout = original 
		
		#creates headers for the test			
		print("Test Input                 Expected output")
		print("")
					
		with open("redirect.txt", "r") as testText:
			line = testText.read() #reads file
			line = line.split("\n")	#creates a list
			line = [i for i in line if i] #removes empty elements
			
			#print(line) #!!! use this to discover listPosition !!!
	
			i = 0 #variable to start loop
			while i != 4:
				try: 
					assert line[listPosition] == printList[i] #assertions
					print(stateList[i].ljust(16) + " ------->      " + line[listPosition] + "\n")
					i += 1
					listPosition += 1
				except AssertionError:
					print("     ERROR  " + stateList[i] + " != " + line[listPosition] + "\n")
					i += 1
					listPosition += 1

if (__name__ == "__main__"):
	foodprep = FoodPrep(itemList=[])
	boundaryAnalysis = BoundaryAnalysis()
	print("          Method: validate_Item\n")
	boundaryAnalysis.item_Boundary()
	print("          Method: validate_Cost\n")
	boundaryAnalysis.cost_Boundary()
