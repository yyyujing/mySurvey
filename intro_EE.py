
def bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return bin(n//2) + bin(n%2)



print(bin(145))



def bin2(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return bin2(n//2) + str(n%2)

print(bin2(145))