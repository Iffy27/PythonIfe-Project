items=('Sugar','Bread (unsliced)','Bread(sliced)','Egg','Three crown(tin)','Peak milk(tin)','Peak milk(sachet)','Bournvita(sachet)','Milo(tin)','Peak milk(large sachet)','Milo(large sachet)','Bornvita(large sachet)','Custard(small sachet)','Golden morn(small sachet)','Corn flakes(small sachet)','Detergent(small wawu)','Detergent(small aerial),''Detergent(big wawu)','Detergent(big aerial)','Corn flakes(big sachet)','Golden morn(large sachet)','Sprite(small)','Pepsi(small)','Fanta(small)','Lacasera(small)','Sprite(big)','Pepsi(big)','Fanta(big)','Lacasera(big)','Coke(big)')
quantity_available=(131,311,229,545,201,230,791,611,367,889,934,758,383,647,121,198,354,323,222,341,458,134,674,757,127,956,374,267,786,546)
price_per_item=(50,200,100,50,150,120,50,50,500,700,700,100,200,100,100,120,115,200,250,750,650,60,80,80,80,150,150,150,150,150)
mydict={}
total=0
def itemsavailable():
	print('Items,quantity available and price per item respectively are:')
	for i,j,k in zip(items,  quantity_available,price_per_item):
		print(i, j, '#',k)
	return
def itemstopurchase():
		for i in range(5):
			purchase=input('What do you want to buy?:')
			if not purchase in items:
				print('Item not in the list') 
			else:
				quantity=int(input('How many do you want?;'))
				query=input('Are you purchasing another item?yes or no:')
				if query=='yes':
					continue
				else:
					pass
					mydict['purchase']=purchase
					mydict['quantity']=quantity
					return mydict
def amountpayable():
	z=int(input('Enter number of items purchased:'))
	total_cost=int(input('Enter total cost'))
	if z<5:
		VAT=0.2*total_cost
		print('VAT',VAT)
		print('Net payable',total_cost+VAT)
	if z>10:
		price=int(input('What is the cheapest price of item you purchased'))
		VAT=0.3*total_cost
		print('VAT',VAT)
		print('Net payable',total_cost+VAT)
	if z>10 and price>=100:
		discount=total_cost-800
		print('Discount:',discount)
		print('Net payable after discount is',discount+VAT)
		return
itemsavailable()
print(itemstopurchase())
amountpayable()
	

