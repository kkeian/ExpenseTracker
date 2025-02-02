from user_in import get_category, get_item, parse_num
from csvparser import get_col
from Category import Category
from Item import Item

filename = "expenses.csv"

print("Expense Tracker")

done = False
categories = []
while (not done):
    category = get_category()
    nextCat = False
    fin = False
    while (not nextCat):
        if fin == 'Y' or fin == 'y':
            nextCat = True
            continue
        item = get_item()
        # Create file input line
        category.add_item(item)
        fin = input(f"Are you done entering items in {category.name}? (Y/N) ")
    categories.append(category)
    fin = input(f"Are you done entering all your items? (Y/N) ")
    if fin == 'Y' or fin == 'y':
        done = True
    
# Store expenses/save data - save to file for now
with open(filename, "w") as f:
    for category in categories:
        f.write(category.serialize())


# Load data
categories = []
last_cat = ""
category = "" # find a way to make string changeable so this is less expensive
cat = None # to hold obj type
with open(filename) as f:
    item = f.readline()
    i = 0
    category, i = get_col(item, i) 
    if category != last_cat: # very expensive here
        if cat != None:
            categories.append(cat)
            last_cat = cat
        cat = Category(category)
    date, i = get_col(item, i)
    name, i = get_col(item, i)
    price, _ = get_col(item, i)
    price = parse_num(price)
    cat.add_item(Item(name, price, date))
categories.append(cat)
    

# Show data
print("Expenses:")
grand_total = 0
for category in categories:
    print(f"  {category.name}:")
    for item in category.items:
        print(f"      {item}")
    total = category.total()
    print(f"    Total: ${total//100}.{total%100}")
    grand_total += total

print(f"Grand total: ${grand_total//100}.{grand_total%100}")
