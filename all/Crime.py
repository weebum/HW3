import csv
with open('crime_train.csv') as trainset:
	train_reader = csv.reader(trainset, delimiter=',')
	first_row = True
	print train_reader
	for row in train_reader:
		if (first_row):
			first_row = False
			continue
		[date, category, _, day, _, _, addr, x, y] = row
		[year, month, _] = date.split(' ')[0].split('-')
		

print "Hell o' Wor'ld!"