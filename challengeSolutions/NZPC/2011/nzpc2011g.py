# Problem G 2011 - Connor Mattson

n = input("How many products will you be entering: ")
while n != '0':
	products = {}
	for i in range(int(n)):
		data = input("Enter the product name, loyalty points required, and days to ship e.g. 'iPodNano 255 1': ").split(' ')
		products[data[0]] = (int(data[1]), int(data[2]))

	customers = int(input("How many customers are to be processed: "))
	customerData = {}
	for i in range(customers):
		customer = input("Enter customer id, number of products, and max waiting time e.g. '1001 2 3' for customer 1001 who is buying 2 items and will wait 3 days: ").split(' ')
		customerData[customer[0]] = [0, False]

		for i in range(int(customer[1])):
			toPurchase = input("What is customer {}'s number {} purchase: ".format(customer[0], i + 1))
			if products[toPurchase][1] <= int(customer[2]): customerData[customer[0]][0] += products[toPurchase][0]
			else: customerData[customer[0]] = [customerData[customer[0]][0], True]

	for customer in customerData.keys():
		print(customer, customerData[customer][0], "*"*int(customerData[customer][1]))
	print("Number of discontented customers is: {}".format(sum([1 for customer in customerData.keys() if customerData[customer][1]])))

	n = input("How many products will you be entering: ")