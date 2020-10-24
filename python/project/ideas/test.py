def sum_primes(lst):
	prime_number = []
	for number in 	lst:


	for div in range(0, ( number + 1)):
			print(number)
		print(div)
		if number & div == 0:
			prime_number.append(number)


	for number in prime_number:
		number_position = prime_number.index(number)
		if number_position == (len(prime_number) - 1):
			break

		result = number + prime_number[number_position + 1]

	print(prime_number)
	print(number_position)
	print(result)

sum_primes([1,2,3,4,5,6,7,8,9,10]);
