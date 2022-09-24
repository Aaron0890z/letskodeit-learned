a = "python"
strn = ""

for i in a:
    strn = i + strn
    print('strn= ', strn)
print(strn)

print("---" * 20)  # ----------------------------------------------


def reverse(string):
    string = string[::-1]
    return string


s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print(reverse(s))

print("---" * 20)  # ----------------------------------------------


def reverse(string):
    string = "".join(reversed(string))
    return string


s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print(reverse(s))

print("---" * 20)  # ----------------------------------------------


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

print("---" * 20)  # ----------------------------------------------

s = "abcd"

print(s[-1::-1])
print(s[-1::-2])
