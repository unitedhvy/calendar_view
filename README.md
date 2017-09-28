Still working on this visualization, looking to add sent/received ratio, also filtering by different senders/groups. 

For this I used google’s takeout to download email archives, then used python to extract email frequency per day to a CSV file. For visualization, I modified D3.js Block 4063318, “Calendar View”, by Mike Bostok.

Instructions:
Import your emails from gmail takeout
Modify mboxtocsv.py with youremail.mbox in the input file area
Run python mboxtocsv.py mboxtocsv.csv
Run python dateformat.py mboxtocsv.csv dateformat.csv
Run python datecount.py dateformat.csv datecount.csv
Modify index.html with appropriate year range (also can change scaling for email count if necessary)
Open index.html with browser

Example 1
![short example](https://github.com/unitedhvy/calendar_view/blob/master/example_1.png)

Example 2
![long example](https://github.com/unitedhvy/calendar_view/blob/master/example_2.png)
