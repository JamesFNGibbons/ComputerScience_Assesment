#A ERP python app
#Written for school controlled assesment 
#Written by James Gibbons <jgibbons@quemit.com>
#Github - https://github.com/JamesGibbons-QuemIT/ComputerScience_Assesment

class interface:
    def askQuestion(self, question):
        get = input(question)
        return get
    
    def showNewCustomerForm(self):
        print("#"*40)
        print("New Customer")
        print("#"*40)
        
        self.newCustomerData = []
        
        try:
            self.newCustomerData.append(str(input("Enter customers name --> ")))
            self.newCustomerData.append(int(input("Enter customers phone -->")))
            self.newCustomerData.apped(str(input("Enter customers email -->")))
            self.enwCustomerData.append(str(input("Enter customers address -->")))
        except(TypeError):
            print("Error - Input data must be the correct data type.")
        
        return self.enwCustomerData
    
    def showOptions(self):
        print("#"*40)
        print("Main menue")
        print("#"*40)
        
        print("1) New Customer")
        return self.askQuestion("Enter a selection ID --> ")

class main:
    def __init__(self):
        self.interface = interface()
        menuSelection = self.interface.showOptions()
        
        if(menuSelection == 1):
            print("Valid!")
    
    def addNewCustomer(self):
        self.newCustomerData = self.interface.
            

def initScript():
    print("Loading program ...")
    main()
    
initScript()
    
        
        