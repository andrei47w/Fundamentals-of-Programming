"""

4. Bank Account

    John wants to manage his bank account. To do this, he needs an application to store all the bank transactions
performed on his account during a month. Each transaction is stored in the application using the following elements:
day (of the month in which the transaction was made, between 0 and 30 for simplicity), amount of money (transferred,
positive integer), type (in - into the account, out – from the account), and description. Write a program that
implements the functionalities exemplified below:

    (A) Add transaction
add <value> <type> <description>
insert <day> <value> <type> <description>
e.g.
add 100 out pizza – add to the current day an out transaction of 100 RON with the "pizza" description
insert 25 100 in salary – insert to day 25 an in transaction of 100 RON with the “salary” description\

    (B) Modify transactions
remove <day>
remove <start day> to <end day>
remove <type>
replace <day> <type> <description> with <value>
e.g.
remove 15 – remove all transactions from day 15
remove 5 to 10 – remove all transactions between days 5 and 10
remove in – remove all in transactions
replace 12 in salary with 2000 – replace the amount for the in transaction having the “salary” description from day 12
with 2000 RON

    (C) Display transactions having different properties
list
list <type>
list [ < | = | > ] <value>
list balance <day>
e.g.
list – display all transactions
list in – display all in transactions
list > 100 - display all transactions having an amount of money >100
list = 67 - display all transactions having an amount of money =67
list balance 10 – compute the account’s balance at the end of day 10. This is the sum of all in transactions,
 from which we subtract out transactions occurring before or on day 10

"""

import datetime

#                                 ================== DOMAIN =====================

def get_length(transactions):
    return len(transactions)

def get_day(transaction):
    return transaction[0]

def get_amount(transaction):
    return transaction[1]

def get_tip(transaction):
    return transaction[2]

def get_desc(transaction):
    return transaction[3]

def sort_t_list(transactions):
    return sorted(transactions, key = lambda tup: tup[0])

def set_amount(transaction, new_amount):
    transaction[1] = new_amount

#                                  ================== FUNCTIONS ==================

def add_transaction(day, amount, tip, desc):
    """
    adds a new transaction to the list
    :param: transaction's day, amount, type and desctription
    """
    if not 0 < day < 30:
        print("Unexpected day of month \n")
        return
    if amount <= 0:
        print("Amount cannot be negative or equal to 0 \n")
        return
    if not (tip == 'in' or tip == 'out'):
        print("Transaction types can only be 'in' or 'out' \n")
        return


    transaction=[]
    transaction.append(day)
    transaction.append(amount)
    transaction.append(tip)
    transaction.append(desc)

    t_list.append(transaction)


def option_a_add(option):
    """
    computes if the command requested is 'add'
    :param: the command as a string
    """
    now = datetime.datetime.now()
    amount = int(option[:option.find(' ')])
    option = option[option.find(' ')+1:]
    tip = option[:option.find(' ')]
    option = option[option.find(' ')+1:]
    desc = option[:-1]

    add_transaction(now.day, amount, tip, desc)


def option_a_insert(option):
    """
    computes if the command requested is 'insert'
    :param: the command as a string
    """
    day = int(option[:option.find(' ')])
    option = option[option.find(' ')+1:]
    amount = int(option[:option.find(' ')])
    option = option[option.find(' ') + 1:]
    tip = option[:option.find(' ')]
    option = option[option.find(' ') + 1:]
    desc = option

    add_transaction(day, amount, tip, desc)


def condition_b(i, tip):
    """
    :return: True or False
    :param: the n th element of the list and the requested command
    """
    tip = tip[:-1]
    if tip.find(' ') == -1 and tip.isdigit() and get_day(t_list[i]) == int(tip): return True
    if tip.find(' ') == -1 and get_tip(t_list[i]) == tip: return True
    if tip.find(' ') != -1 and int(tip[:tip.find(' ')]) < get_day(t_list[i]) < int(tip[tip.find(' ')+3:]): return True
    return False


def option_b_remove(tip):
    """
    computes if the command requested is 'remove'
    :param: the command as a string
    """
    pos = int(0)
    for i in range(get_length(t_list)):
        if condition_b(pos, tip):
            del t_list[pos]
            pos-=1
        pos+=1


def option_b_replace(option):
    """
    computes if the command requested is 'replace'
    :param: the command as a string
    """
    day = int(option[:option.find(' ')])
    option = option[option.find(' ')+1:]
    tip = option[:option.find(' ')]
    option = option[option.find(' ')+1:]
    desc = option[:option.find(' ')]
    option = option[option.find(' ') + 1:]
    option = option[option.find(' ') + 1:]
    ok=False
    new_amount=int(option)
    for i in range(get_length(t_list)):
        if get_day(t_list[i]) == day and get_tip(t_list[i]) == tip and get_desc(t_list[i]) == desc:
            ok=True
            set_amount(t_list[i], new_amount)
    if ok == False:
        raise ValueError("There are no such transactions")


def compute_day(day):
    """
    computes if the command requested is 'list balance'
    :param: day as an int
    """
    sum=int(0)
    i=int(0)
    while get_day(t_list[i]) <= day:
        if get_tip(t_list[i]) == 'in':
            sum+=get_amount(t_list[i])
        else:
            sum-=get_amount(t_list[i])
        i+=1
    print("     Account’s balance at the end of day", day, "was", sum)


def condition_c(i, tip):
    """
    :return: True or False
    :param: the n th element of the list and the requested command
    """
    if tip=='': return True
    if tip[:2]=='in' and get_tip(t_list[i]) == 'in': return True
    if tip[:3]=='out' and get_tip(t_list[i]) == 'out': return True
    if tip[:1]=='<' and get_amount(t_list[i]) < int(tip[2:]): return True
    if tip[:1]=='>' and get_amount(t_list[i]) > int(tip[2:]): return True
    if tip[:1]=='=' and get_amount(t_list[i]) == int(tip[2:]): return True
    return False


def option_c(tip):
    """
    computes if the command requested is 'list'
    :param: the command as a string
    """
    if tip[:7] == 'balance':
        day = int(tip[8:])
        compute_day(day)
        return

    if get_length(t_list) == 0:
        print("     All transactions have been deleted")
        return
    pos=int(0)
    for i in range(get_length(t_list)):
        if condition_c(i, tip):
            pos+=1
            print(pos, '.  day: ',get_day(t_list[i]),
                  ';  amount: ', get_amount(t_list[i]),
                  ' RON;  type: ', get_tip(t_list[i]),
                  ';  description: ', get_desc(t_list[i]), sep='')


#                                   ===================== UI ======================

def print_menu ():
    print("\n             MENU: \n"
          "Add transaction: \n"
          "     add <value> <type> <description> \n"
          "     insert <day> <value> <type> <description> \n"
          "Modify transactions \n"
          "     remove <day> \n"
          "     remove <start day> to <end day> \n"
          "     remove <type> \n"
          "     replace <day> <type> <description> with <value> \n"
          "Display transactions having different properties \n"
          "     list \n"
          "     list <type> \n"
          "     list [ < | = | > ] <value> \n"
          "     list balance <day> \n"
          "Exit program \n"
          "     exit \n \n")

    option=str(input())
    option+=' '
    temp_op=str(option[:option.find(' ')])
    if temp_op == 'add':
        option_a_add(str(option[4:]))
    elif temp_op == 'insert':
        option_a_insert(str(option[7:]))
    elif temp_op == 'remove':
        option_b_remove(option[7:])
    elif temp_op == 'replace':
        option_b_replace(option[8:])
    elif temp_op == 'list':
        option_c(str(option[5:]))
    elif temp_op == 'exit':
        exit('  Bye!')
    else: print("    The command you entered does not exist. Try again")


#                                      =================== TESTS =====================

def set_up():
    """
    sets up all the already known transactions
    """
    add_transaction(1, 35, "out", "pizza")
    add_transaction(4, 3500, "in", "salary")
    add_transaction(5, 100, "out", "groceries")
    add_transaction(16, 210, "out", "tax")
    add_transaction(17, 120, "out", "gasoline")
    add_transaction(19, 1000, "in", "deposit")
    add_transaction(21, 140, "out", "groceries")
    add_transaction(26, 23, "out", "fastfood")
    add_transaction(26, 230, "out", "clothes")
    add_transaction(29, 45, "out", "book")
    return t_list


def test_add_transaction():
    """
    tests if the transactions are correct
    """
    for i in range(get_length(t_list)):
        day=get_day(t_list[i])
        amount=get_amount(t_list[i])
        tip=get_tip(t_list[i])
        if not 0<day<30:
            raise ValueError("Unexpected day of month \n")
        if amount <=0:
            raise ValueError("Amount cannot be negative or equal to 0 \n")
        if not (tip=='in' or tip=='out'):
            raise ValueError("Transaction types can only be 'in' or 'out' \n")


def test_get_length():
    """
    tests if the length is correct
    """
    if not get_length(t_list) == 10:
        raise ValueError("Wrong number of transactions")


def test_all():
    """
    computes all the available tests
    """
    test_add_transaction()
    test_get_length()

if __name__ == '__main__':
    print("Hello A3 \n")

    t_list=[]
    t_list=set_up()
    test_all()

    while True:
        print_menu()
        t_list = sort_t_list(t_list)