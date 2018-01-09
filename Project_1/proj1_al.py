#Comment at top of file includes proper identifying information,
#a description of the problem, and a description of the important
#points of your solution

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
	
#	print(output)
			
main()

#What I learned and what difficulties
