import csv

"""
fh = open("test.csv",'rt')

try:
    reader = csv.reader(fh)
#    print "Data form the CSV:", list(reader)
    data = list(reader)
    print "Data cells from CSV:"
    print data[0][0]
    print data[0][1]
    print data[0][2]

    print data[1][0], data[1][1], data[1][2]

except Exception as e:
        print "Exception is:",e
finally:
    fh.close()
"""



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



names = ["Test1", "Test2","test3"]
grades = ["C" , "A","B"]
f = open("csv_write.csv",'wt')
f2 = open("csv_writer_with_tabs.csv",'wt')

print "Available Dialects:", csv.list_dialects()
try:
    writer = csv.writer(f)
    writer2 = csv.writer(f2, delimiter='\t',lineterminator='\n\n')

    writer.writerow(('Sr','Names','Grades'))
    writer2.writerow(('Sr','Names','Grades'))

    for i in range(3):
        writer.writerow((i+1,names[i], grades[i]))
        writer2.writerow((i+1,names[i], grades[i]))

finally:
    f.close()
    f2.close()
