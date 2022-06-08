import mysql.connector as connection
def connecttosql():
    try:
        mydb = connection.connect(host="localhost", user="root", passwd="admin",use_pure=True)
         # check if the connection is established
         # print(mydb.is_connected())
         # mydb.close()
    except Exception as e:
        print(str(e))



def 
try:

    mydb = connection.connect(host="localhost", database='Student', user="root", passwd="admin", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "UPDATE studentdetails SET FirstName = 'Kumar', LastName = 'Gaurav' WHERE Studentid = 1122"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    mydb.commit()

    #let's check if the value is updated in the table.
    query = "Select * from studentdetails where Studentid=1122;"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))