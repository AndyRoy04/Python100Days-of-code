def prime_check(number):
    prime = True
    if number == 2:
        print(f"{number} is a prime number")
    elif number%2==0:
        print(f"{number} is not a prime number")
    elif number%2==1:
        for i in range(2, number):
            if number%i==0:
                prime = False
            # else:
            #     prime = True
        if prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")
n = int(input("Check this number : "))
prime_check(number=n)