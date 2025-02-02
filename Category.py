class Category:
    def __init__(self, name):
        self.name = name
        self.items = []


    def add_item(self, item):
        self.items.append(item)
        
    
    def serialize(self):
        # for output to file
        out = self.name
        for item in self.items:
            out += "," + item.serialize() + "\n"
        return out
    

    def total(self):
        sum = 0
        for item in self.items:
            sum += item.price
        return sum
        

    def __str__(self):
        # for output to console
        out = self.name + "\n"
        for item in self.items:
            out += "  " + item + "\n"
        return out