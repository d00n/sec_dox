#!/usr/bin/python

import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost', user='root', passwd='carrotcake55', db='ring')
cursor = mydb.cursor()

with open('h') as csvfile:	
    reader = csv.DictReader(csvfile)
   
    for row in reader:
#	print 'sym: ' + row['Symbol']
        cursor.execute('INSERT INTO company(\
          symbol, \
          name, \
          market_cap, \
          sector, \
          industry )' \
          'VALUES("%s", "%s", "%s", "%s", "%s")' % 
          (row['Symbol'].strip(), row['Name'], row['MarketCap'], row['Sector'], row['industry']) )

mydb.commit()
cursor.close()
print "Done"
