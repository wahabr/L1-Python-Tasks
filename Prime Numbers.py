guess = int(input("What is your number?"))
a = 1
b = 2
c = 1
while a <= guess:
    a += 1
    b = 2
    while b <= guess:
        if guess == a * b:
            b += 1
        elif guess == 1:
            b += 1
        else:
            c = 2
            b += 1
if c == 1:
    print("{} is not a prime number".format(guess))
else:
    print("{} is a prime number".format(guess))










