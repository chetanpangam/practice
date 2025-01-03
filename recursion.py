from datetime import datetime

def tri_recursion(k):
	if(k>0):
		result = k + tri_recursion(k-1)
		#print(result)
	else:
		result=0
		
	return result
t1 = datetime.now()
print("tri_recursion", tri_recursion(75))
t2= datetime.now()
print(t2-t1)

def Sum_Recursion(n):
	if n == 0:
		return 0
	
	return n + Sum_Recursion(n-1)

t3= datetime.now()
print("Sum_Recursion", Sum_Recursion(75))
t4= datetime.now()
print(t4-t3)


def wrapper(n):
	dp = [0] * (n+1)

	def Sum_Recursion1(n):
		if n == 0:
			return 0
		
		if n in dp:
			return dp[n]
		
		dp[n] = n + Sum_Recursion1(n-1)
	
		return dp[n]
	
	return Sum_Recursion1(n)


t5= datetime.now()
print("wrapper", wrapper(75))
t6= datetime.now()
print(t6-t5)