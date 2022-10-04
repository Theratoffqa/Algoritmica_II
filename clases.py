class User:

    def __init__(self,user,password,name,lastname,mail):
        self.user = user
        self.password = password
        self.name = name
        self.lastname = lastname
        self.mail = mail

    def verify_session(self):
        pass


class Client(User):

    def __init__(self,paycard):
        
        self.paycard = paycard
        
    
    def register_client(self):
        pass
    

    def update_info(self):
        pass

    
class Admin(User):

    def __init__(self,masterKey):
        self.masterKey = masterKey
       
        

    def update_catalogue(self):
        pass
    

class Payment: 
    
    def __init__(self,number,concept,dni,date,amount):
        self.number = number
        self.concept = concept
        self.dni = dni 
        self.date = date
        self.amount = amount


    def register_transaction(self):
        pass



class Reserve:
    
    def __init__(self,code,entryDate,depDate,numDays,people): 
        self.code = code
        self.entryDate = entryDate
        self.depDate = depDate
        self.numDays = numDays
        self.people = people

        
    def reserve(self):
        pass


    def show_reservation(self):
        pass


    def change_state(self):
        pass

    def verify_state(self):
        pass
    

class Room:
    
    def __init__(self,state,price,roomtype,roomnumber): 
        self.state = state
        self.price = price
        self.roomtype = roomtype
        self.roomnumber = roomnumber

    def view_info(self):
        pass
