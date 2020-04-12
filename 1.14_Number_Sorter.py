even = []
odd = []
non_whole = []



for i in range(10):
    num = eval(input("Please enter a number: "))
    if num % 2 == 0:
        even.append(num)
    elif num % 2 == 1:
        odd.append(num)
    else:
        non_whole.append(num)
print("The results are: ")
print("Evens:", even)
print("Odds:", odd)
print("Others: ",non_whole)
