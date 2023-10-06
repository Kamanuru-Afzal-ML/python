class Account:
    def __init__(self,firstname,lastname):
        self.fname=firstname
        self.lname=lastname
    def showFullname(self):
        print("Full name:",self.fname,self.lname)
    def changeName(self,newname):
        self.lname=newname
user=Account('Afzal','Kamanuru')
user.showFullname()
user.changeName('AFZAL')
del user   #deleting instance



