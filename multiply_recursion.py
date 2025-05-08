def multiply(x,y):
    if y == 0:
        return 0
    else:
        return x + multiply(x,y-1)

print(multiply(5,3))
#Expected output is 15