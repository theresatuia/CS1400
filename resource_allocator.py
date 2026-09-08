colonists_num =int(input('How many citizens: '))
food_num = int(input('How many total units: '))
total_rations = colonists_num * 3
remaining_units = food_num - total_rations
mira_num = round(((remaining_units * 0.13)), 2)
tov_num = round((remaining_units - mira_num) * 0.11, 2)
final_units = food_num - (mira_num + tov_num)
crew_num = round((final_units/colonists_num), 2)
mira_share = round((mira_num + crew_num), 2)
tov_share = round(tov_num + crew_num, 2)


print("Mira's share: " + str(mira_share))
print("Tov's share: " + str(tov_share))
print("Crew's share: " + str(crew_num))