arr = list(map(int, input('head=').split()))
n = int(input('n='))

if n == len(arr):
    print(arr[1:])
else:
    arr.pop(-n)
    print(arr)
