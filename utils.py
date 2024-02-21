def factorial(n): 
	for i in range(1, n + 1):
		fact *= i
	return fact

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

def is_power_of_five(num):
    while num % 5 == 0 and num != 0:
        num /= 5
    return num == 1

def is_power_of_two(num):
    return num and (not(num & (num - 1)))
