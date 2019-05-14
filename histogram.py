n = int(input())
count = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

for i in range(n):
	i = int(input())
	if i < 200:
		count_1 = count_1 + 1
		p1 = (count_1 / n) * 100
	elif i >= 200 and i <= 399:
		count_2 = count_2 + 1
		p2 = (count_2 / n) * 100
	elif i >= 400 and i <= 599:
		count_3 = count_3 + 1
		p3 = (count_3 / n) * 100
	elif i >= 600 and i <= 799:
		count_4 = count_4 + 1
		p4 = (count_4 / n) * 100
	elif i >= 800:
		count_5 = count_5 + 1
		p5 = (count_5 / n) * 100

print("{0:.2f}".format(p1) + "%")
print("{0:.2f}".format(p2) + "%")
print("{0:.2f}".format(p3) + "%")
print("{0:.2f}".format(p4) + "%")
print("{0:.2f}".format(p5) + "%")
