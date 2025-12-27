N = int(input())

width = len(bin(N)) - 2  

for i in range(1, N + 1):
    dec_val = str(i)
    oct_val = oct(i)[2:]
    hex_val = hex(i)[2:].upper()
    bin_val = bin(i)[2:]

    print(dec_val.rjust(width + 4),
          oct_val.rjust(width + 4),
          hex_val.rjust(width + 4),
          bin_val.rjust(width + 4))
