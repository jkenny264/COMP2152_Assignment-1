"""
# i
#Author: John Kenny
#Assignment: #1
"""


# ii
gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 #int
membership_active = True # bool

# iii
# this variable is a dictionary. The Keys of the dictionary are strings. The Values of the dictionary are integer tuples.
workout_stats = {"Alex":(30, 45, 20), "Jamie":(20, 15, 10), "Taylor":(90, 90, 10)}

# iv
# i created a temporary dict to store the calculated total values, and then I
# I add all the calculated total values to the workout_stats dictionary.
temp_stats = {}
for x in workout_stats:
    total = 0
    for j in workout_stats[x]:
        total = total + j
    temp_stats[str(x+"_Total")]=total
for x in temp_stats:
    workout_stats[x] = temp_stats[x]    

# v
# I wasn't sure exactly how to handle this part.
# The instructions state to include the total workout minutes calculations in the workout_stats dictionary, 
# so I needed a way to exclude those values when adding the individual (non-totaled) workout minutes to this 2D list.
# I chose to check for each key in the workout_stats dictionary, if it contains the substring "_Total".
workout_list = []
for x in workout_stats:
    if "_Total" not in x:
        workout_list.append(list(workout_stats[x]))
# workout_list is a list of lists of integers. It is a 2-dimensional (nested) list containing integers.


# vi
print("Yoga and running exercise minutes: ")
for row in workout_list:
    print(row[0:2])
print("")
print("weightlifting exercise minutes: ")
for row in workout_list[1:3]:
    print(row[2:3])
print("")

# vii
# I created this list to hold the friends' names because I couldn't think of a way to print the correct name without it.
friends = ["Alex", "Jamie", "Taylor"]
for i in range(len(workout_list)):
    total = 0
    for num in workout_list[i]:
        total += num
    if total >= 120:
        print ("Great job staying active, " + friends[i] + "!")
print("")

# viii
search_term = input("Please enter the name of the person who's workout minutes you are searching for: ")
print("")
if search_term not in workout_stats:
    print(f"Friend {search_term} not found in the records.")
else:
    print(f"{search_term}'s workout minutes:")
    print(f"yoga: {workout_stats[search_term][0]}")
    print(f"running: {workout_stats[search_term][1]}")
    print(f"weightlifting: {workout_stats[search_term][2]}")
print("")

# ix
highest = None
highest_friend = ""
lowest = None
lowest_friend = ""
for x in workout_stats:
    if "_Total" in x:
        if ((highest == None) or (highest < workout_stats[x])):
            highest = workout_stats[x]
            highest_friend = x.replace("_Total", "")
        if ((lowest == None) or (lowest > workout_stats[x])):
            lowest = workout_stats[x]
            lowest_friend = x.replace("_Total", "")
print(f"friend with the highest total workout minutes: {highest_friend}")
print(f"friend with the lowest total workout minutes: {lowest_friend}")
        
    