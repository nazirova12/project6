def card_type(card_number):
	if not (len(card_number) > 12 and len(card_number) < 17):
		return False

	digit = card_number[0]
	if digit in '23456':
		if digit == '2': return 'Платежная система "МИР"'
		if digit == '3' and card_number[1] == '7': return 'American Express'
		if digit == '4': return 'Visa'
		if digit == '5': return 'MasterCard'
		if digit == '6': return 'Discover'
	return False


def sum_of_digits(num):
	if num < 10:
		return num
	else:
		return sum_of_digits(num % 10 + sum_of_digits(num // 10))


def number_check(card_number):
	summa = 0
	for i in range(1,len(card_number)+1):
		digit = int(card_number[-i])
		if i % 2 == 0:
			summa += sum_of_digits(2 * digit)
		else:
			summa += digit

	if summa % 10 == 0:
		return True

	return False


def main():
	card_number = input('Please enter your card number:')
	# card_number = ''
	card_number = card_number.replace(' ', '')
	type_of_card = card_type(card_number)
	if type_of_card:
		print('Card type:' + type_of_card)
		if number_check(card_number):
			print('Card number - ' + card_number + 'is VALID!!!')
	else:
		print('Card number - ' + card_number + 'is WRONG!!')
		print('Please try again!')
		main()

if __name__ == '__main__':
	main()