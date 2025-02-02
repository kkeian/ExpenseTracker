from Item import Item
from Category import Category
date_form = ("mm/dd/yyyy")
date_prompt = f"Enter date ({date_form}): "
amount_prompt = "Enter the amount spent: "

def get_category():
    name = input("Enter the expense category: ")
    return Category(name)


def get_item():
    name = input("Enter the expense item short name: ")
    amt = input(amount_prompt)
    amt, valid_amt = _validate_amt(amt)
    while (not valid_amt):
        amt = input(amount_prompt)
        amt, valid_amt = _validate_amt(amt)
    date = input(date_prompt)
    valid_date = _validate_date(date)
    while (not valid_date):
        date = input(date_prompt)
        valid_date = valid_date(date)
    return Item(name, amt, date)


def _validate_date(date):
    dlen = len(date)
    longest = len(date_form)
    if (dlen > longest or dlen < longest-2):
        return False
    date_t = [0,0]
    i = 0
    section = 0
    num = ""
    while (section < 2): # don't parse year because we naively assume all values are valid
        if date[i] == '/':
            date_t[section] = int(num)
            i += 1
            section += 1
            num = ""
            continue
        num += date[i]
        i += 1
    if date_t[0] < 1 or date_t[0] > 12:
        return False
    if date_t[1] < 1 or date_t[1] > 31:
        return False
    return True
        

def parse_num(amt):
    num = 0
    char_count = len(amt)
    multiplier = pow(10, (char_count-2))
    # parse amount into accurate decimal number with assumed decimal
    i = 0
    while (i < char_count):
        if amt[i] == '.':
            i += 1
            continue
        num += multiplier * int(amt[i])
        multiplier /= 10
        i += 1
    return num

    
def _validate_amt(amt):
    # format = 400 = 4.00
    coded_num = parse_num(amt)
    while int(coded_num) < 0:
        return (None, False)
    return (coded_num, True)