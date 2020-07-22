n = int(input('Enter number of days: '))
price = []

for i in range(n):
	price.append(float(input()))

max_profit = 0

for i in range(n):
	min_val = price[i]
	max_val = price[i]
	for j in range(i+1, n):
		if price[j]>max_val:
			max_val = price[j]
	if max_val - min_val > max_profit:
		max_profit = max_val - min_val
		day = i+1

if max_profit>0:
	print('Maximum profit possible = ', max_profit)
	print('Earliest buy date: ', day)
