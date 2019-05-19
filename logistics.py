cargo_number = int(input())
average_price = 0
cargo_sum = 0
minibus = 0
truck = 0
train = 0
for cargo in range(0, cargo_number):
        cargo = int(input())
        cargo_sum = cargo_sum + cargo
        if cargo <= 3:
                minibus = minibus + cargo
        elif cargo > 3 and cargo <= 11:
                truck = truck + cargo
        elif cargo > 11:
                train = train + cargo
percent_minibus = (minibus / cargo_sum) * 100
percent_truck = (truck / cargo_sum) * 100
percent_train = (train / cargo_sum) * 100
average_price = (minibus * 200 + truck * 175 + train * 120) / cargo_sum

print("{:.2f}".format(average_price))
print("{:.2f}".format(percent_minibus) + "%")
print("{:.2f}".format(percent_truck) + "%")
print("{:.2f}".format(percent_train) + "%")
