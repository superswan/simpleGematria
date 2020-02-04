# Gets user input and converts to lowercase
user_input = input("Please enter a word or phrase you would like to find the simple english gematria of: ")
word = user_input.lower()


total = []
for n in word: 
	
	if n == 'a':
		total.append(1)
		print('A = 1')
		
	elif n == 'b':
		total.append(2)
		print('B = 2')
		
	elif n == 'c':
		total.append(3)
		print('C = 3')
		
	elif n == 'd':
		total.append(4)
		print('D = 4')
		
	elif n == 'e':
		total.append(5)
		print('E = 5')

	elif n == 'f':
		total.append(6)
		print('F = 6')

	elif n == 'g':
		total.append(7)
		print('G = 7')

	elif n == 'h':
		total.append(8)
		print('H = 8')

	elif n == 'i':
		total.append(9)
		print('I = 9')

	elif n == 'j':
		total.append(10)
		print('J = 10')

	elif n == 'k':
		total.append(11)
		print('K = 11')

	elif n == 'l':
		total.append(12)
		print('L = 12')

	elif n == 'm':
		total.append(13)
		print('M = 13')

	elif n == 'n':
		total.append(14)
		print('N = 14')

	elif n == 'o':
		total.append(15)
		print('O = 15')

	elif n == 'p':
		total.append(16)
		print('P = 16')

	elif n == 'q':
		total.append(17)
		print('Q = 17')

	elif n == 'r':
		total.append(18)
		print('R = 18')

	elif n == 's':
		total.append(19)
		print('S = 19')


	elif n == 't':
		total.append(20)
		print('T = 20')

	elif n == 'u':
		total.append(21)
		print('U = 21')

	elif n == 'v':
		total.append(22)
		print('V = 22')

	elif n == 'w':
		total.append(23)
		print('W = 23')

	elif n == 'x':
		total.append(24)
		print('X = 24')

	elif n == 'y':
		total.append(25)
		print('Y = 25')

	elif n == 'z':
		total.append(26)
		print('Z = 26')

sumtotal = sum(total)

print(f"Your word's simple english gematria sums to: {sumtotal}")

	
	



