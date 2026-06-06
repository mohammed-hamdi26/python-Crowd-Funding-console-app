
class User:
    def __init__(self, fname,lname, email,password,mobile=None, id=None):

      
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.mobile = mobile

    def to_dict(self):
 
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "password": self.password,
            "mobile": self.mobile
            
        }