
import ast

line = input().strip()
stones = ast.literal_eval(line.split("=")[1].strip())

def canReachLastStone(stones):
    reachable = 0
    for i in range(len(stones)):
        if i > reachable:
            return False
        reachable = max(reachable, i + stones[i])
    return True

print(str(canReachLastStone(stones)).lower())
