import csv


fh = open("test.csv",'rt')

try:
    reader = csv.reader(fh)
    print "Data form the CSV:", list(reader)

    data = list(reader)
    print "Data cells from CSV:"

    #Stupid manual print
    print data[0][0]
    print data[0][1]
    print data[0][2]

    print data[1][0], data[1][1], data[1][2]

except Exception as e:
        print "Exception is:",e
finally:
    fh.close()

