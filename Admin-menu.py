items=['Sugar','Bread (unsliced)','Bread(sliced)','Egg','Three crown(tin)','Peak milk(tin)','Peak milk(sachet)','Bournvita(sachet)','Milo(tin)','Peak milk(large sachet)','Milo(large sachet)','Bornvita(large sachet)','Custard(small sachet)','Golden morn(small sachet)','Corn flakes(small sachet)','Detergent(small wawu)','Detergent(small aerial),''Detergent(big wawu)','Detergent(big aerial)','Corn flakes(big sachet)','Golden morn(large sachet)','Sprite(small)','Pepsi(small)','Fanta(small)','Lacasera(small)','Sprite(big)','Pepsi(big)','Fanta(big)','Lacasera(big)','Coke(big)']
quantity_available=[131,311,229,545,201,230,791,611,367,889,934,758,383,647,121,198,354,323,222,341,458,134,674,757,127,956,374,267,786,546]
price_per_item=[50,200,100,50,150,120,50,50,500,700,700,100,200,100,100,120,115,200,250,750,650,60,80,80,80,150,150,150,150,150]
def itemsavailable():
	print('Items,quantity available and price per item respectively are:')
	for i,j,k in zip(items,  quantity_available,price_per_item):
		print(i, j, '#',k)
	return
def change_price_of_items():
	query=input('Are you the admin,Yes or No:')
	if query=='Yes':
		print('Welcome admin')
		x=input('What is the name of item:')
		if not x in items:
			print(x,'not in items')
		else:
			y=int(input('Old price of %s  is:' %(x)))
			z=int(input('New price:'))
			print('The new price of %s is #%i' % (x,z))
	else:
		print('Access denied')
		return
def addmore():
	query=input('Are you the admin,Yes or No:')
	if query=='Yes':
		print('Welcome admin')
		x=input('Add more items:')
		items.append(x)
		print(items)
	else:
		print('Access denied')
	return
def afterstock():
	for i in items:
		x=input('What items have been purchased?')
		items.remove(x)
		print(items)
		return
itemsavailable()
change_price_of_items()
addmore()
afterstock()

