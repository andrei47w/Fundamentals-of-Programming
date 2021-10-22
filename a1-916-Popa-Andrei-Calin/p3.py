"""
Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,...
obtained from the sequence of natural numbers by replacing composed numbers
with their prime divisors, without memorizing the elements of the sequence.
"""

def search_nth_elem(n):
    """
    searches the nth element of the sequence
    """
    nr=int(0)   #current number which will/won't be replaced by its prime divisors
    pos=int(0)  #postition in the sequence
    while n!=pos:
        nr+=1
        if nr<4:
            pos+=1
        else:
            cnr=int(nr) #copies nr so it isn't lost
            ok=0
            for i in range(2,nr//2+1): #searches for nr's prime divisors
                if cnr%i==0:
                    ok=1
                    while cnr%i==0:
                        cnr/=i
                    pos+=1
                if n==pos:
                    print("the n-th element of the sequence is: ", i, end="")
                    return
            if not ok:  #if nr is prime
                pos+=1
                if n==pos:
                    print("the n-th element of the sequence is: ", cnr, end="")
                    return
    print("the n-th element of the sequence is: ", n, end="")
    return

if __name__ == "__main__":
    print("give n: ", end="")
    n=int(input())
    search_nth_elem(n)
