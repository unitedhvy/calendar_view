import sys
import mailbox
import csv

writer = csv.writer(open(sys.argv[1], "wb"))
for message in mailbox.mbox('uttam408.mbox'): #customize here w/ your mbox file
	writer.writerow([message['subject'], message['from'], message['date']])
#	writer.writerow([message['subject'], message['from'], message['date'], message.get_payload()])
