def main():
    print("Fibo")


if __name__ == '__main__':
    main()

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please give +ve integers")
elif nterms == 1:
    print("Fibo seq upto ", nterms, " is ", n1)
else:
    print("Fibo seq is: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
