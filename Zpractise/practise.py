num = 1234
reversed_num = 0

while num != 0:
    a = num % 10
    reversed_num = reversed_num * 10 + a
    num //= 10
print(reversed_num)

num = 9876
print(str(num)[::-1])
# --------------------------------------

num = 8
fact = 1
count = 1

for i in range(num):
    fact = fact * count
    count += 1
print(fact)

a = 8
c = 1
for i in range(1, a + 1):
    c = c * i
print(c)

# --------------------------------------

nterm = 8
n1, n2 = 0, 1

count = 0
while count < nterm:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

# -----------------------------
n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("\r")

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("\r")
for i in range(n, -1, -1):
    for j in range(0, i+1):
        print("*", end="")
    print("\r")
