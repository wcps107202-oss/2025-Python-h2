def factorial(n):
    if n == 1:
        #print(n)
        return 1
    #else:
       #print(n)
    return  n * factorial(n - 1)

print(factorial(5)) # factorial(5) = 5 *4 *3 *2 *1
