import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date
#Michelle Perez 
#PSID:132116
#this is to connect to the SQL database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("cis3368dbid.cc9zm0jrngaw.us-east-1.rds.amazonaws.com", "mperez39", "Krowczyk0531!", "CIS3368db")
        
#this is where the python code begins
#this is the simple function of the menu for the user
def menu():
    print("""
        MENU
        a - Add contact
        d - Remove contact
        u - Update contact details
        b - Output all contacts in alphabetical order
        c - Output all contacts by creation date
        o - Output all contacts
        q - Quit
        """)


def option1(): #here is the code to add a contact to the table
    adding = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('%s','%s')"
    results = execute_read_query(connection, adding)
    for result in results:
        print(result)
        print("Contact added.")

def option2(): #here the user gets to choose which row to delete by using the id
    id_to_delete = '%s'
    delete = "DELETE FROM contacts WHERE id = %s" % (id_to_delete)
    execute_query(connection, delete)
    print("Contact removed.")

def option3(): #for this option I am updating the contacts using the id
    new_id = '%s'
    update_id = """
    UPDATE contacts
    SET contactDetails = %s
    WHERE id = %s """ % (new_id)
    execute_query(connection, update_id)
    print("Contact updated.")

def option4(): #this option will order the contacts in alphabetical order
    alpha ="""
     SELECT * FROM contacts
     ORDER_BY contactDetails;
     """
    execute_read_query(connection, alpha)
    print("Contacts in alphabetical order.")

def option5(): #this option will order the contacts in numerical order of the date
    creation ="""
    SELECT * FROM contacts
    ORDER_BY creationDate;
    """
    execute_read_query(connection, creation)
    print("Contacts in creation date order.")

def option6(): #this option pulls up the table from sql
    select_contact = "SELECT contactDetails, creationDate FROM contacts;"
    results = execute_read_query(connection, select_contact)
    for result in results:
        print(result)

menu()
option = input("Choose an option: ")
#this part of the code connects to the menu and the different options the user can choose
while option != "q":
    if option == "a": 
        option1()
    elif option == "d":
        option2()
    elif option == "u":
        option3()
    elif option == "b":
        option4()
    elif option == "c":
        option5()
    elif option == "o":
        option6()
    else:
        print("Invalid selection, try again...")

    print()
    menu()
    option = input("Choose an option: ")

print("Goodbye!") 

