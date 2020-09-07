numbers = [] 
increments = 0

def sd1(r):
	i = 0
	while i < r:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i