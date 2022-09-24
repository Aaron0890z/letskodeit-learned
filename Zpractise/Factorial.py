# Python program to find the factorial of a number provided by the user.

# change the value for a different result
#num = 7

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
# -------------------Second logic--------------------------------------
count = 1
fact = 1
for i in range(num):
    fact = fact * count
    count += 1
print("The factorial of", num, "is", factorial)


list = [5,4,3,2,1]
for i in list:
    list.sort(reverse=False)
print(list)

a = list
print(max(a))