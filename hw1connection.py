import mysql.connector
from mysql.connector import Error
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


class Contacts:
    contactList = []
    def __init__(self, id, contact_details, creation_date):
        self.id = id
        self.contactDetails = contactDetails
        self.creationDate = creationDate

    def menu(): 
        ans = True
        while ans:
    # this is the simple menu function
            print("--------------------------------------------------------------------") 
            print("\t\t\tMENU", flush=False) 
            print("--------------------------------------------------------------------")  
            print("a - Add contact") 
            print("d - Remove contact") 
            print("u - Update contact details") 
            print("b - Output all contacts in alphabetical order") 
            print("c - Output all contacts by creation date") 
            print("o - Output all contacts") 
            print("q - Quit") 

        ans = int(input("Choose an option: ")) 
      
        return ans

    def add_contact(self):
        if ans=='a':
            print("\nContact added")
    def remove_contact(self):
        elif ans=='d':
            print("\nContact removed")
    def update_contact(self):
        elif ans=='u':
            print("\nContact details updated")
    def output_alphabetic(self):
        elif ans=='b':
            print("\nContacts in alphabetical order")
    def output_creation_date(self):
        elif ans=='c':
            print("\nContacts by creation date")
    def output_contacts(self):
        elif ans=='o':
            print("\nAll contacts")
        select_contacts = "SELECT * FROM contacts"
        results = execute_read_query(connection, select_contacts)
        for result in results:
            print(result)

    def quit():
        elif ans=='q':
            print("\nQuitting...")
            ans==None

        else:
            print("\nNot Valid, try again...")
