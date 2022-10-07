
class User:

    def __init__(self,user,password,name,lastname,mail):
        self._user = user
        self._password = password
        self._name = name
        self._lastname = lastname
        self._mail = mail

    def verify_session(self):
        pass


class Client(User): 

    def __init__(self,paycard):
        
        self._paycard = paycard
        
    
    def register_client(self):
        pass
    

    def update_info(self):
        pass

    
class Admin(User):

    def __init__(self,masterKey):
        self._masterKey = masterKey
       
        

    def update_catalogue(self):
        pass
    

class Payment: 
    
    def __init__(self,number,concept,dni,date,amount):
        self._number = number
        self._concept = concept
        self._dni = dni 
        self._date = date
        self._amount = amount


    def register_transaction(self):
        pass



class Reserve:
    
    def __init__(self,code,entryDate,depDate,numDays,people): 
        self._code = code
        self._entryDate = entryDate
        self._depDate = depDate
        self._numDays = numDays
        self._people = people

        
    def reserve(self):
        pass


    def view_reservation(self):
        pass


    def change_state(self):
        pass

    def verify_state(self):
        pass
    

class Room:
    
    def __init__(self,state,price,roomtype,roomnumber): 
        self._state = state
        self._price = price
        self._roomtype = roomtype
        self._roomnumber = roomnumber

    def view_info(self):
        pass


