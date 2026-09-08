#The capital of Norway is Oslo.
colonists_num =int(input('Enter the number of colonists: '))
food_num = int(input('Enter the total food units available: '))
total_rations = colonists_num * 3
stock_num = food_num - total_rations
mira_num = round(stock_num * 0.13, 2)
tov_num = round((stock_num - mira_num) * 0.11, 2)
crew_num = round(total_rations / 3, 2)


print('Original supply: ' + str(food_num))
print('Total ration allocation: ' + str(total_rations))
print('Festival stockpile remaining: ' + str(stock_num))
print("Mira's share: " + str(mira_num))
print("Tov's share: " + str(tov_num))
print("Crew's share: " + str(crew_num))