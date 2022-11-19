distance = float(input("How many kilometers did you run? \n"))
hours = int(input("What was your finish time? Enter hours: \n"))
minutes = int(input("Enter minutes: \n"))

distance_miles = distance / 1.61
time_total_minutes = 60 * hours + minutes
time_total_hours = hours + minutes / 60

pace_in_mins = time_total_minutes / distance_miles
sceonds = int((time_total_minutes % distance_miles) * 60)
pace_in_hours = distance_miles / time_total_hours

print(str(round(distance_miles, 2)) + " miles", str(round(pace_in_mins)) + ":" + str(sceonds) + " pace", str(round(pace_in_hours, 2)) + " MPH")



# 



