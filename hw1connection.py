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
        
    # this is the simple menu function
 
class Contacts:
    contact_list = []
    def main():
        print("""
        MENU
        a - Add contact
        d - Remove contact
        u - Update contact details
        b - Output all contacts in alphabetical order
        c - Output all contacts by creation date
        o - Output all contacts
        q - Quit

        Choose an option: """)
        ans = input()

    def __init__(self, id, contact_details, creation_date):
        self.id = id
        self.contact_details = contact_details
        self.creation_date = creation_date


    def add_contact(self):
        if ans=='a':
            print("\nContact added")
        query = "INSERT INTO contacts (, contactDetails, creationDate) VALUES (, '%s', %s)"
        execute_query(connection, query)
        

    def remove_contact(self):
        if ans=='d':
            print("\nContact removed")
        delete = "DELETE FROM contacts WHERE id = %s"
        execute_query(connection, delete)

    def update_contact(self):
        if ans=='u':
            print("\nContact details updated")
        update="""
        UPDATE contact
        SET contactDetails = %s
        Where id = 5;
        """
        execute_read_query(connection, update)

    def output_alphabetic(self):
        if ans=='b':
            print("\nContacts in alphabetical order")
        alpha ="""
        SELECT * FROM contacts
        ORDER_BY contactDetails;
        """
        execute_read_query(connection, alpha)

    def output_creation_date(self):
        if ans=='c':
            print("\nContacts by creation date")
        creation ="""
        SELECT * FROM contacts
        ORDER_BY creationDate;
        """
        execute_read_query(connection, creation)

    def output_contacts(self):
        if ans=='o':
            print("\nAll contacts")
        select_contacts = "SELECT * FROM contacts"
        results = execute_read_query(connection, select_contacts)
        for result in results:
            print(result)

    def quit(self):
        if ans=='q':
            print("\nQuitting...")
            ans==None

        else:
            print("\nNot Valid, try again...")
