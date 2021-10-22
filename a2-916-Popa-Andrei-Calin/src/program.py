"""

Implement a menu-driven console application that provides the following functionalities:

1    Read a list of complex numbers (in z = a + bi form) from the console.
2    Display the entire list of numbers on the console.
3    Display on the console the longest sequence that observes a given property.
4    Exit the application.

Sequence Properties

7    The difference between the modulus of consecutive numbers is a prime number.
8    The modulus of all elements is in the [0, 10] range.

"""

import math
import sys


#==================== domain =====================


def get_real(nr):
    return complex_list[nr][0]

def get_imag(nr):
    return complex_list[nr][1]

def get_length():
    return len(complex_list)

def modulus(nr):
    return float(math.sqrt(get_real(nr)**2 + get_imag(nr)**2))

def condition(i,op):
    op=int(op)
    if op==3:
        return is_prime(abs(modulus(i) - modulus(i+1))) and modulus(i+1).is_integer() and modulus(i).is_integer()
    else:
        return 0<=modulus(i)<=10 and modulus(i).is_integer()

def search(op):
    # searches sequences for option 3 or 4
    # returns length or the sequence and the last element's position
    
    op=int(op)
    count=0
    last_pos=0
    max_count=0
    list_length=int(get_length())
    if op==3:
        list_length-=1
    for i in range(list_length):
        if condition(i,op):
            count+=1
        else:
            if count>=max_count:
                max_count=count
                last_pos=i
            count=0
    if count>=max_count:
        max_count=count
        last_pos=i+1
    return max_count, last_pos


def is_prime(x):
    # checks if number is prime
    # param: int x
    # returns True is x is prime and false otherwise
    
    x=abs(x)
    if x > 1:
        for i in range(2,int(x/2)):
             if (x % i) == 0:
                return False
        return True
    return False


def read_complex_nr(i):
    # reads complex number
    # param: int i which represents the ith complex number from the list 
    
    complex_nr=()
    print('\n', i+1, ".  ", end="")
    a=int(input("give a: "))
    complex_nr+=(a,)
    b=int(input("      give b: "))
    complex_nr+=(b,)
    complex_list.append(complex_nr)

#====================== ui =======================



def menu():
    # prints the menu
    
    print('\n','\n',"1. Read a list of complex numbers (in z = a + bi form) from the console")
    print(" 2. Display the entire list of numbers on the console")
    print(" 3. Display on the console the longest sequence that observes that the difference between the modulus of consecutive numbers is a prime number")
    print(" 4. Display on the console the longest sequence that observes the modulus of all elements is in the [0, 10] range")
    print(" 5. Exit the application", '\n')

    op=input("  input what you want to do: ")
    
    if op=='1':
        option1()
    elif op=='2':
        option2()
    elif op=='3':
        option3()
    elif op=='4':
        option4()
    elif op=='5':
        sys.exit("  bye!")
    else:
        print("    Invalid operation. Try again")


def print_nr(nr):
    # prints a complex number
    # param: complex number x
    
    print(get_real(nr),"+", get_imag(nr), end="")
    print("*i", end="")

#================== operations ==================



def option1():
    nr_of_complex = int(input("how many complex numbers do you want to input? \n"))
    for i in range(0,nr_of_complex):
        read_complex_nr(i)


def option2():
    for i in range(0,get_length()):
        print(i+1, ".  ", end="")
        print_nr(i)
        print()


def option3():
    count=int(search(3)[0])
    last=int(search(3)[1])
    if count == 0:
        print("there are no such sequences")
        return

    print("the sequence is: ", end="")
    for i in range(last-count, last+1):
        print_nr(i)
        print(", ", end="")


def option4():
    count=int(search(4)[0])
    last=int(search(4)[1])
    if count == 0:
        print("there are no such sequences")
        return

    print("the sequence is: ", end="")
    for i in range(last-count, last):
        print_nr(i)
        print(", ", end="")

#==================== main ======================


if __name__ == '__main__':
    
    complex_list=[(4,3),(7,0),(-3,4),(10,0),(0,10),(-10,0),(4,3),(7,0),(9,6),(23,9)]
    while True:
        menu()
