def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        countdown(n-1)

countdown(5)
#Outputs:
# 5
# 4
# 3
# 2
# 1