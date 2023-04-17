n = int(input("Call a number: "))

def fibonacci(n):

	f0 = 0
	f1 = 1

	if n == 1:
		fn = 0

	elif n == 2:
		fn = 1

	else:
		for r in range(n-2):
			fn = f0 + f1
			f0 = f1
			f1 = fn

	return fn

print(fibonacci(n))