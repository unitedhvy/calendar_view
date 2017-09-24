#date as YEAR-MON-DAY

import sys

infile = open(sys.argv[1]) #input a converted MBOX csv
outfile = open(sys.argv[2], 'w') #desired output file

for line in infile:

	splits = line.split(",")

	date = splits[len(splits)-1]
	date = date[1:13]

	year_loc = date.find("201")

	if (year_loc != -1):
		month = date[year_loc-4:year_loc-1]
		year = date[year_loc:year_loc+4]
		day = date[year_loc-7:year_loc-5]

		#cleaning			
		if (day == ""):
			day = "0" + date[year_loc-6:year_loc-5]
		if (len(day) == 1):		
			day = date[year_loc+5:year_loc+7]
		if (" " in day): 
			day = "0"+day[1:]

		#switch month to number
		month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12" }	
		if month in month_dict:
			date = year + "-" + month_dict[month] + "-" + day
			print date
			row = date + "\n"
			outfile.write(row)


infile.close()
outfile.close()	