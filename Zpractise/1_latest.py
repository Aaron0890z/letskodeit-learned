nth = int(input("How many terms "))

a = 0
b = 1
count = 0

if nth <= 0:
    print("Cannot do for negative integers")
elif nth == 1:
    print("Fibo of one term is ", a)
else:
    print("Fibo seq is: ")
    while count < nth:
        print(a)
        nterm = a + b
        a = b
        b = nterm
        count += 1

# -----------------------------------------

a = 12345
rev_num = 0

while a != 0:
    digit = a % 10
    rev_num = rev_num * 10 + digit
    a //= 10

print(rev_num)

# -----------------------------------------

s = "abcd"

str = ""

for i in s:
    str = i + str
    print(str)