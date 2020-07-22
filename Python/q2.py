number = int(input("Enter a palindrome: "))
n = str(number)
middle = int((len(n)/2))

def roundOff(n):
	length = len(str(n))
	print('length ', length)
	increment = 10**(int(length/2) +1)
	print('increment ', increment)
	return (int(n/increment)+1)*increment

if n[middle] =='9':
	print('Number ',number)
	n = str(roundOff(number))
	middle = int(len(str(n))/2)
	if len(n)%2 != 0:
		n = n[:middle] + n[middle] + n[:middle][::-1]
	else:
		n = n[:middle] + n[:middle][::-1]

else:
	n = [int(d) for d in str(n)]

	if len(n)%2 !=0:
		n[middle] = n[middle] + 1

	else:
		if n[middle-1]!=9 & n[middle]!=9:
			n[middle-1] = n[middle-1] +1
			n[middle] = n[middle] +1



palindrome = ''.join(str(e) for e in n)
print('The next smallest palindrome is: ',palindrome) 
