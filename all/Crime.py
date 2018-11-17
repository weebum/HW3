import csv

# range: 0 ~ 49
def month2quarter(year, month):
	months = (int(year) - 2003) * 12 + int(month)
	return months / 4

# range: 8 x 6 (@ default unit length = 0.02)
def dd2splits(x, y, unit=0.02):	
	delta_x = int((x + 122.52) / unit) # (x - min_x) / 0.02
	delta_y = int((y - 37.82) / unit)  # (y - min_y) / 0.02
	return (delta_x, delta_y)
	
def quarter_cols():
	qlist = []
	for i in range(50):
		qlist.append("quar" + str(i))
	return qlist
	
def split_cols(unit=0.02):
	assert (unit % 0.005 == 0.0)
	slist = []
	for x in range(int(0.16 / unit)):
		for y in range(int(0.12 / unit)):
			slist.append("split" + str(x) + "_" + str(y))
	return slist
	


with open('crime_train.csv') as original, open('my_crime_dataset.csv', mode='w') as preprocessed:
	reader = csv.reader(original, delimiter=',')
	writer = csv.writer(preprocessed, delimiter=',')
	is_first_row = True
	for row in reader:
		if (is_first_row):
			new_row = quarter_cols() + ["Category", "DayOfWeek", "PdDistrict"] + split_cols()
			writer.writerow(new_row)
			is_first_row = False
			continue
		
		[date, category, _, day, _, _, addr, x, y] = row
		[year, month, _] = date.split(' ')[0].split('-')
		quarters = []
		for i in range(50):
			if (i < month2quarter(year, month)):
				quarters.append(
			
		

print "Hell o' Wor'ld!"