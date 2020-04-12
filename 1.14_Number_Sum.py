total = 0
while True:
    num = input("Please enter a number or STOP: ")
    if num.upper() == "STOP":
        break
    else:
        total += int(num)
print("The total sum is", str(total))
