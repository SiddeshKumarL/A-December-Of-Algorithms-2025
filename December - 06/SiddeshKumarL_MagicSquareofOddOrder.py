def generate_magic_square(n):
    if n % 2 == 0:
        print("Magic square is only possible for odd values of n.")
        return

    M = n * (n * n + 1) // 2
    print(f"Magic constant: {M}")

    magic_square = [[0 for _ in range(n)] for _ in range(n)]

    i = n // 2
    j = n - 1

    num = 1
    while num <= n * n:
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magic_square[i][j] != 0:
            j -= 2
            i += 1
            continue
        else:
            magic_square[i][j] = num
            num += 1

        i -= 1
        j += 1

    for row in magic_square:
        print(" ".join(f"{x:2d}" for x in row))


n = int(input("Enter n: "))
generate_magic_square(n)
