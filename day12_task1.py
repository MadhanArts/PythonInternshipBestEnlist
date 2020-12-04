import sqlite3
import json

# Create a database or connect to an existing database
con = sqlite3.connect("test.db")
print("Opened database successfully")

# Create table using cursor
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE MADHAN"
                   "("
                   + "dictinary BLOB,"
                   + "list BLOB,"
                   + "tuple BLOB,"
                   + "string varchar(50),"
                   + "Integer INTEGER,"
                   + "flo FLOAT,"
                   + "Bool BOOLEAN,"
                   + "None BLOB"
                     ");")
except Exception as e:
    print("Error :", e)
else:
    print("Table created")

# Inserting data values into table using Json
datafile = open("sample.json", "r")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]),
            float(row[5]), bool(row[6]), row[7])
    dataframe.append(data)

try:
    cursor.executemany("INSERT INTO MADHAN VALUES (?,?,?,?,?,?,?,?)", dataframe)
except Exception as e:
    print("Error : ", e)
else:
    con.commit()
    print("Data inserted")

# Displaying values of data in database
try:
    cursor.execute("SELECT * from MADHAN")
except Exception as e:
    print("Error : ", e)
else:
    for row in cursor.fetchall():
        print(row)

# Deleting database
# con.execute("DROP TABLE MADHAN")
# print("Table deleted")

# Closing connection
con.close()
