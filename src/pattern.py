
# Print the pattern

for n in range(1, 10):
    if n <= 5:
        print(*('*' * n))
    else:
        print(*('*' * (10 - n)))