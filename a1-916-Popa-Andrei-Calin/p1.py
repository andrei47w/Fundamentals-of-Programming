"""
Generate the first prime number larger than a given natural number n.
"""

def is_prime(x):
    """
    checks if x is a prime number
    returns true/false
    """
    if x > 1:
        for i in range(2,int(x/2)):
             if (x % i) == 0:
                return False
        return True
    return False

def search_prime(x):
    """
    searches all the numbers larger than x until it finds a prime
    prints the prime number
    """
    while True:
        x+=1
        if is_prime(x):
            print("first prime number larger than n is:", x)
            return

if __name__ == "__main__":

    print("give n: ", end="")
    x=int(input())
    search_prime(x)

