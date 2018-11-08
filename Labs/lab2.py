import datetime
str(datetime.datetime.now())

class Item(object):
    def __init__(self, __name, __price, __taxable):
        self.name = __name
        self.price = __price
        self.taxable = __taxable

    def __str__(self):
        return " ".join(str(x) for x in (self.name, self.price, self.taxable))

    def getPrice(self):
        return self.price

    def getTax(self):
        if self.taxable == True:
            a = self.tax_rate * self.price
        return a

class Receipt(object):
    def __init__(self, __tax_rate, __purchases):
        self.tax_rate = __tax_rate
        self.purchases = __purchases

    def __str__(self):
        rec = ''
        for x in self.purchases:
            recline = "{:_>20}{}".format(x, x.getPrice())
            rec += recline + '\n'
        return rec

    def addItem(self):

        return

print('Welcome to Receipt Creator')
more = True
while more == True:
    name = input('Enter Item Name:')
    price = input('Enter Item Price:')
    tax = input('Is the item taxable (yes/no):')
    item = input('Add another item (yes/no):')
    if item == 'no':
        more = False
    else:
