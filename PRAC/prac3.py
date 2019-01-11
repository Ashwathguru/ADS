#Design and implement billing software for Super Market. Here items fall into 0%, 5%, 10% and 20% GST. Essential day to day items like wheat, rice, dals, salt, sugar fall in 0% bracket. Soaps & detergents, tooth paste, cooking oils, cookies & biscuits are in 5% category. Shampoos, cosmetics, ready to eat items are in 10% tax slab. TV, washing machines, refrigerator are in 20% bracket. Provide method to add items into stock. Data to be stored are item name, tax rate, unit price and quantity. There should be provision to change the unit price, tax rate and update quantity. Customer can choose any listed products and should get bill. In addition to purchased item detail, bill amount should include the total GST applied to selected items.

class SuperMarket:
	def __init__(self):
		self.available_items={'1001':['wheat',30,1,20],'1002':['rice',50,1,5],'1003':['dals',90,1,10],'1004':['salt',40,1,25],'2001':['sugar',80,1.05,20],'2002':['Soaps_detergents',100,1.05,23],'2003':['tooth_paste',20,1.05,20],'2004':['cooking_oils',200,1.05,20],'2005':['cookies_biscuits',50,1.05,30],'3001':['Shampoos',150,1.10,30],'3002':['cosmetics',200,1.10,10],'3003':['ready to eat items',100,1.10,50],'4001':['TV',32000,1.20,5],'4002':['washing_machines',15000,1.20,2],'4003':['refrigerator',20000,1.20,6]}
		self.customer_kart=[]

	def customer_add_item(self,id):
		if id in self.available_items.keys():
			n,p,t,q=self.available_items[id]
			if q>0:
				self.customer_kart.append(id)
				n,p,t,q=self.available_items[id]
				q-=1
				self.available_items[id]=[n,p,t,q]
			else:
				print("OUT OF STOCK")
		else:
			print("ITEM UNAVAILABLE")
	def change_tax(self,id,new_tax):
		if id in self.available_items.keys():
			n,p,t,q=self.available_items[id]
			t=new_tax
			self.available_items[id]=[n,p,t,q]
		else:
			print("ITEM UNAVAILABLE")
	def change_price(self,id,new_price):
		if id in self.available_items.keys():
			n,p,t,q=self.available_items[id]
			p=new_price
			self.available_items[id]=[n,p,t,q]
		else:
			print("ITEM UNAVAILABLE")

	def generate_bill(self):
		tot=0
		raw_tot=0
		for k in self.customer_kart:
			print("***************************************************************************************")
			n,p,t,q=self.available_items[str(k)]
			price=p
			print("ITEM_ID: ",k)
			print("ITEM_NAME: ",n)
			print("PRICE: ",p)
			print("TAX: ",t)
			raw_tot+=price
			price=price*t
			print("FINAL PRICE: ",price)
			tot+=price
		tot_gst=tot-raw_tot
		print("TOTAL GST: ",tot_gst)
		print("TOTAL BILL: ",tot)

sm=SuperMarket()
sm.customer_add_item('1001')
sm.customer_add_item('1002')
sm.customer_add_item('2001')
sm.customer_add_item('3001')
sm.customer_add_item('3003')
sm.customer_add_item('4002')

sm.change_tax('4002',1.30)

sm.change_price('4002',25000)

sm.generate_bill()
