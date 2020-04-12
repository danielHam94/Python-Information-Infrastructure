lower = eval(input("Please enter a lower bound (int): "))
upper = eval(input("Please enter an upper bound (int): "))
div = eval(input("Please enter a number to divide by (int): "))

result = [num for num in range(lower,upper) if num % div == 0]

print(result)
