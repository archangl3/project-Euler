def stupid_solver(n):
    prev = 1
    curr = 2

    sum_ = 2
    while curr < n:
        prev, curr = curr, prev + curr

        if curr % 2 == 0:
            sum_ += curr

    return sum_


print(stupid_solver(4*10**6))