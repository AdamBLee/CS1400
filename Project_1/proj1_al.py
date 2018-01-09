# Name: Adam Lee
# Class: CS-1400-X01 
# Description of Problem: Create a tip calculator that will display several tip options and total amounts based on the cost of a meal that the user inputs
# Important points of solution: I defined several functions that helped simplify the main method.  The calculate_tip and calculate_total methods were used so that I could call them inline. I also used string formatting to be able easily output the correct rounded decimal numbers in a single line.

from decimal import Decimal

TIP_EXCELLENT = .20
TIP_AVERAGE = .15
TIP_POOR = .10

def calculate_tip(tip_percentage, meal_cost):
	
	tip = meal_cost * tip_percentage
	
	return tip
	
def calculate_total(tip, meal_cost):
	
	return round(Decimal(meal_cost + Decimal(tip)),2)
	
def get_decimal_format(number_to_format):
	
		return round(Decimal(number_to_format), 2)	
	
def main():
	
	user_input = input('Enter the cost of the meal: ')
	
	user_input_list = user_input.split(' ')

	meal_cost = float(user_input_list[1])
	
	tip_excellent_calculated = calculate_tip(TIP_EXCELLENT, meal_cost)
	
	tip_average_calculated = calculate_tip(TIP_AVERAGE, meal_cost)

	tip_poor_calculated = calculate_tip(TIP_POOR, meal_cost)					
	
	meal_cost = round(Decimal(meal_cost), 2)

	print('Cost of meal: ${0}'.format(meal_cost))
	print('Excellent Service tip: ${0} total: ${1}'.format(get_decimal_format(tip_excellent_calculated),calculate_total(tip_excellent_calculated,meal_cost)))
	print('average Service tip: ${0} total: ${1}'.format(get_decimal_format(tip_average_calculated),calculate_total(tip_average_calculated,meal_cost)))
	print('Poor Service tip: ${0} total: ${1}'.format(get_decimal_format(tip_poor_calculated),calculate_total(tip_poor_calculated,meal_cost)))
	
					
main()

#What I learned and what difficulties: One of the big problems I was running into was that some of my output wasn't being formatted the way that I expected.  I kept running the program, and then going back to my code, convinced that my output was somehow wrong.  I realized after several minutes that I was calling the 'get_decimal_format()' method on the wrong variables.  I was using the same variable twice on the lines that I was printing out to the console.  I am doing a lot with those lines, and was not looking closely enough at which variable I was trying to format to two decimal places.  While I like the efficiency of calculating everything in the print line, it does make it more difficult to keep track of exactly what I am doing  
