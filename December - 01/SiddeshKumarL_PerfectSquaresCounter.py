import math

N = int(input())

squares = []
limit = int(math.sqrt(N))

for k in range(1, limit + 1):
    squares.append(k * k)

print(*squares)
print(len(squares))
