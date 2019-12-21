sum = 0
f = input("Enter a word: ")
for i in f:
	if i == 'f':
		print(sum)
		sum = sum + 1
	else:
		sum = sum + 1
		continue