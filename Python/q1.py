d = int(input("Enter a number: "))

def is_prime(n):
	c=0
	if n==1:
		return 0
	for i in range(2,n):
		if n%i==0:
			c += 1
	if c==0:
		return n
	else:
		return 0

for k in range(10**(d-1), 10**d):
	if is_prime(k)!=0:
		if is_prime(k+2)!=0:

			print(k, k+2)

with open("myFirstFile.txt") as text_file:
    print(k, k+2, file=text_file)