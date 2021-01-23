

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def divide(a,b):
	if b == 0:
		return 0
	else:
		return a/b

if __name__ == "__main__":
	add(1,3)
	sub(3,1)
	mul(1,5)
	divide(10,2)
