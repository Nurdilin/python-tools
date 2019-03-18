import csv

fh2 = open("test.csv",'rt')

try:
    reader = csv.DictReader(fh2)
    #DictReader() , which will treat the first
    #row values as column names. These column names act as a key in the dictionary
    #where the data gets stored

    for row in reader:
        print row['first_name'], row['email']


    print "Columns            :", reader.fieldnames
    print "Dialect            :", reader.dialect
    print "Current line       :", reader.line_num
    print "Rewinding          :"
    fh2.seek(0)
    print "Current line       :", reader.line_num
    print "Movint to next line:"
    reader.next()
    print "Current line       :", reader.line_num

    for row in reader:
        print row['first_name'], row['email']

finally:
    fh2.close()
