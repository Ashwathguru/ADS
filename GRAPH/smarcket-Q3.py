## Design and implement billing software for Super Market. Here items fall into 0%, 5%, 10% and 20% GST. Essential day to day items like wheat, rice, dals, salt, sugar fall in 0% bracket. Soaps & detergents, tooth paste, cooking oils, cookies & biscuits are in 5% category. Shampoos, cosmetics, ready to eat items are in 10% tax slab. TV, washing machines, refrigerator are in 20% bracket. Provide method to add items into stock. Data to be stored are item name, tax rate, unit price and quantity. There should be provision to change the unit price, tax rate and update quantity. Customer can choose any listed products and should get bill. In addition to purchased item detail, bill amount should include the total GST applied to selected items.

class market:

    def __init__(self):
        self.stock = []
    
    def addstock(self,item):
        self.stock.append(item)

    def update_stock(self,item):
        for old in self.stock:
            if item['name'] == old['name']:
                for k,v in item.items():
                    old[k] = v
                
    def get_stock(self):
        for item in self.stock:
            print(item)

    def generate_bill(self,itemlist):
        gtotal,gtax = 0,0
        for item in itemlist:
            for it in self.stock:
                if item['name'] == it['name']:
                    if it['quantity'] >= item['quantity']:
                        item['price'] = item['quantity']*it['unit_price']
                        item['tax'] = (item['price'] * it['tax_rate'] / 100 )
                        item['total'] = item['price'] + item['tax']
                        it['quantity'] = it['quantity'] - item['quantity']
                        gtotal += item['price']
                        gtax += item['tax']
        return (itemlist,gtotal,gtax)

def main():
    shop = market()
    it = {'name':'Salt','unit_price':10,'tax_rate':0,'quantity':100}
    shop.addstock(it)
    i2 = {'name':'Salt','quantity':200}
    shop.update_stock(i2)
    it2 = {'name':'Sugar','unit_price':20,'tax_rate':0,'quantity':50}
    it3 = {'name':'Biscuit','unit_price':10,'tax_rate':5,'quantity':100}
    it4 = {'name':'Shampoo','unit_price':100,'tax_rate':10,'quantity':30}
    it5 = {'name':'TV','unit_price':50000,'tax_rate':20,'quantity':5}
    shop.addstock(it2)
    shop.addstock(it3)
    shop.addstock(it4)
    shop.addstock(it5)
    shop.get_stock()
    bill1 = [{'name':'Salt','quantity':2},{'name':'Biscuit','quantity':3}]
    bill = shop.generate_bill(bill1)
    print(bill[0],"\nPrice -->",bill[1],"\nTotal GST -->",bill[2],"\nAmount -->",bill[1]+bill[2])
    shop.get_stock()


if __name__ == "__main__":
    main()