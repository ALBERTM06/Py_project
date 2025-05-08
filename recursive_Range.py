def countdown(x,y):
    if x == (y-1):
        return
    else:
        print(x)
        countdown(x-1,y)
countdown(10,2)

#The above code uses recursion to countdown numbers within a specified range