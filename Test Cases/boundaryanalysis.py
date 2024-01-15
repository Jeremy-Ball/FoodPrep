import sys
from unittest import mock
from foodprep import *

class BoundaryAnalysis():
	
	def __init__(self):
		self.self = self
		
#------------------------------------------

	def main_menu_boundary(self):
		#define input values and expected print statements then put them in lists
	
		stateList = [] #values to mock
		printList = [] #statment to assert
		
		#this is where the program should begin reading assertions. Set to begin where print statements begin occuring
		listPosition = 6
		
		state1 = ".9"
		print1 =  ("Not a valid option.")
		
		state2 = "1.1"
		print2 = ("Not a valid option.")
		
		state3 = "3.9"
		print3 = ("Not a valid option.")
		
		state4 = "4.1"
		print4 = ("Not a valid option.")
		
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
					foodprep.main_menu() #method to test
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
				assert line[listPosition] == printList[i] #assertions
				print("    "  + stateList[i].ljust(5) + " ------->      " + line[listPosition] + "\n")
				i += 1

#---------------------------------------------------

	def month_Boundary(self):
		#define input values and expected print statements then put them in lists
	
		stateList = [] #values to mock
		printList = [] #statment to assert
		
		#this is where the program should begin reading assertions. Set to begin where print statements begin occuring
		listPosition = 0
		
		state1 = ".9"
		print1 =  ("Invalid input")
		
		state2 = "00"
		print2 = ("Invalid input")
		
		state3 = "12.1"
		print3 = ("Invalid input")
		
		state4 = "13"
		print4 = ("Invalid input")
		
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
					FoodPrep(itemList = []).validateMonth() #method to test
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
					print("    "  + stateList[i].ljust(5) + " ------->      " + line[listPosition] + "\n")
					i += 1
					listPosition += 1
				except AssertionError:
					print("     ERROR  " + stateList[i] + " != " + line[listPosition] + "\n")
					i += 1
					listPosition += 1
					
#--------------------------------------------					

	def day_Boundary(self):
		#define input values and expected print statements then put them in lists
	
		stateList = [] #values to mock
		printList = [] #statment to assert
		
		#this is where the program should begin reading assertions. Set to begin where print statements begin occuring
		listPosition = 0
		
		state1 = ".9"
		print1 =  ("Invalid input")
		
		state2 = "00"
		print2 = ("Invalid input")
		
		state3 = "31.1"
		print3 = ("Invalid input")
		
		state4 = "32"
		print4 = ("Invalid input")
		
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
					FoodPrep(itemList = []).validateDay() #method to test
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
					print("    "  + stateList[i].ljust(5) + " ------->      " + line[listPosition] + "\n")
					i += 1
					listPosition += 1
				except AssertionError:
					print("     ERROR  " + stateList[i] + " != " + line[listPosition] + "\n")
					i += 1
					listPosition += 1

#---------------------------------------------------------
		
if __name__ == "__main__":
	foodprep = FoodPrep(itemList=[])
	boundaryAnalysis = BoundaryAnalysis()
	print("          Method: main_menu\n")			
	boundaryAnalysis.main_menu_boundary()
	print("          Method: validate_Month\n")
	boundaryAnalysis.month_Boundary()
