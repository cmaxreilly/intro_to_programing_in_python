import sys



# Python program to print all Primes Smaller 
# than or equal to N using Sieve of ERatosthenes
#def seive_of_eratosthenes(upper_limit):
#    list_of_numbers = list(range(0, upper_limit))
#    list_of_primes = [1, 2]
#    for prime in list_of_primes:
#        for number in list_of_numbers:
#            if number % prime == 0:
#                pass
#            else:
#                list_of_primes.append(number)
#
#    return list_of_primes

#print(seive_of_eratosthenes(100))


def sieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not 
        # changed, then it is a prime
        if (prime[p] == True):

            #Updating all mltiple of p
            for i in range(p * p, num+1, p):
                prime[i] = False

        p += 1

    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)

# Driver code

if __name__ == '__main__':
    num = int(sys.argv[1]) 
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    sieveOfEratosthenes(num)

