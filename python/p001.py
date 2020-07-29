def stupid_solver(n):
	return sum([i for i in range(n) if (i % 3 == 0) or (i % 5 == 0)])

print(stupid_solver(1000))