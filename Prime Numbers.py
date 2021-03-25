guess = int(input("What is your number?"))
a = 1
b = 2
c = 1
while a <= guess:
    a += 1
    b = 2
    while b <= guess:
        if guess == a * b:
            c = 2
        b += 1
if guess == 1:
    c = 2
if c == 2:
    print("{} is not a prime number".format(guess))
else:
    print("{} is a prime number".format(guess))











