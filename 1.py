def ontime(n):
    iterations = 0
    for i in range(1,n+1):
        iterations += 1
    print("when n is",n,"iterations =",iterations)
ontime(10)
ontime(20)
ontime(42)
print("\n with every 'n' the time taken and iteration will increase")