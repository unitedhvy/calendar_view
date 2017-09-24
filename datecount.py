#counts the occurrences of each date, generates a new csv with these counts

import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')
date_dict = {}

outfile.write("Date" + "," + "Count" + "\n") #header

for line in infile:

	date = line[:10]
	if date not in date_dict:
		date_dict[date] = 1
	else:
		date_dict[date] = date_dict[date] + 1

for date in date_dict:
	row = date + "," + str(date_dict[date]) + "\n"
	print row
	outfile.write(row)


infile.close()
outfile.close()	