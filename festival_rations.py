colonists_num =int(input('Enter the number of colonists: '))
food_num = int(input('Enter the total food units available: '))
total_rations = colonists_num * 3
stock_num = food_num - total_rations


print('Original supply: ' + str(food_num))
print('Total ration allocation: ' + str(total_rations))
print('Festival stockpile remaining: ' + str(stock_num))
