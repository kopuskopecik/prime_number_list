# listing prime numbers
a = input("Please enter a positive integer more than 1 for listing prime numbers: ")
while not a.isdigit() or int(a) == 1 or int(a) == 0:
    a = input("Please enter a positive integer more than 1 for listing prime numbers: ")
a = int(a)

prime_number_list = []

for number in range(2, a + 1):
    counter = 0
    if number == 2:
        prime_number_list.append(number)
    
    else:    
        for i in range(2, number):
           
            if number % i == 0:
                #print(a, "is a not prime number")
                counter+= 1
                break
        if not counter:
            #print(a, "is a prime number")
            prime_number_list.append(number)
print(prime_number_list)