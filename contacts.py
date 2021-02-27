class Contacts:
    contactList = []
    def __init__(self, id, contactDetails, creationDate):
        self.id = id
        self.contactDetails = contactDetails
        self.creationDate = creationDate

def menu(): 
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

        choice = int(input("Choose an option: ")) 
      
        return choice 