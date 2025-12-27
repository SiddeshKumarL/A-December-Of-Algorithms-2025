def count_students_unable_to_eat(students, sandwiches):
    from collections import Counter

    cnt = Counter(students)

    for s in sandwiches:
        if cnt[s] == 0:
            break
        cnt[s] -= 1

    return cnt[0] + cnt[1]




students = list(map(int, input().split()))

sandwiches = list(map(int, input().split()))

ans = count_students_unable_to_eat(students, sandwiches)
print(ans)
