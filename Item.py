class Item:
    def __init__(self, name, price, date):
        self.name = name
        self.price = int(price) # stored with an assume decimal
        self.date = date


    def _price_out_form(self):
        change = self.price % 100
        whole_num = self.price // 100
        return f"{whole_num}.{change}"


    def serialize(self):
        return f"{self.date},{self.name},{self._price_out_form()}"

    
    def __str__(self):
        return f"{self.date} - {self.name} {self._price_out_form()}"