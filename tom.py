import math
holidays = int(input())

working_days = 365 - holidays
total_play_minutes = (working_days * 63) + (holidays * 127)
diffrence = math.fabs(30000 - total_play_minutes)
hours = int(diffrence // 60)
minutes = int(hours % 60)

if total_play_minutes > 30000:
	print("Tom will run away")
	print(f"{hours} hours and {minutes} minutes for play")
else:
	print("Tom sleeps well")
	print(f"{hours} hours and {minutes} minutes less for play")
