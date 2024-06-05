# DP_Fibonacci.py

FibArray = [0, 1]

def fibonacci(n):
	if n <= 1:
		return n

	elif n<= len(FibArray):
		# print(f"elif n = {n}")
		return FibArray[n-1]
	else:
		# print(f"else n = {n}")
		temp_fib = fibonacci(n-1)+fibonacci(n-2)
		FibArray.append(temp_fib)
		# print(FibArray)
		return temp_fib
	# print(FibArray)

# Driver Program

memo = [0 for i in range(100)]
def fib(n):
	if n <= 1:
		return n
	if memo[n] != 0:
		return memo[n]
	else:
		memo[n] = fib(n-1) + fib(n-2)
		return memo[n]	
	



print(fibonacci(6))
print(fib(6))