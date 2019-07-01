# read_csv.py 
import csv 
with open('hackers.csv', 'r', newline='') as myCsvFile:    
reader = csv.reader(myCsvFile, delimiter=',', quotechar='|') 
      for row in reader.readlines(): 
            print('row = ', row)
			
---------------------------------------------------------------------

# read_csv.py 
import csv 
with open('hackers.csv', 'r', newline='') as myCsvFile: 
     reader = csv.DictReader(myCsvFile) 
          for row in reader.readlines(): 
                print(row['column_name_1'], row['column_name_2'])
				
-----------------------------------------------------------------------

# read_csv.py 
import csv 
with open('hackers.csv', 'r', newline='') as myCsvFile: 
       reader = csv.DictReader(myCsvFile) 
       for row in loc_reader: 
               for (k, v) in row.items(): 
                     print(k, ':', v)

# read_csv.py 
import csv 
with open('hackers.csv', 'r') as myCsvFile:   
      next(myCsvFile) 
      for row in myCsvFile.readlines(): 
             print(row)
			
# write_csv.py 
import csv 
with open('hackers.csv', 'w') as myCsvFile: 
    columns = ['column_name_1', 'column_name_2'] 
    writer = csv.DictWriter(myCsvFile, fieldnames=columns)    
    writer.writeheader() 
    writer.writerow({'column_name_1': 'Mark', 'column_name_2': 'Twain'}) 
     writer.writerow({'column_name_1': 'Foo', 'column_name_2: 'Bar'})
					  
					  
