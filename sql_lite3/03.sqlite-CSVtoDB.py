import csv, sqlite3

input_file = 'sql_lite3/input.csv'

conn = sqlite3.connect('sql_lite3/suppliers.db')
c = conn.cursor()

file_reader = csv.reader(open(input_file,'r'),delimiter = ',')
header = next(file_reader,None)
print(header)

for row in file_reader:
    data = []
    for idx in range(len(header)):
        data.append(row[idx])
    c.execute('insert into suppliers values(?,?,?,?,?)',data)

conn.commit()

output = c.execute('select * from suppliers')
rows = output.fetchall()
print('행의 갯수 : ',len(rows))
for row in rows:
    print("필드의 갯수 : ",len(row))
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)