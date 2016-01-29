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
        print("New Employee")
        print("#"*40)
        
        self.newCustomerData = []
        
        try:
            self.newCustomerData.append(str(raw_input("Enter employee's ID -->")))
            self.newCustomerData.append(str(raw_input("Enter employee's name --> ")))
            self.newCustomerData.append(str(raw_input("Enter employee's phone -->")))
            
            self.type = str(raw_input("Enter employee's Type (AP/FQ) -->"))
            if(self.type == "AP"):
                self.newCustomerData.append(str("Apprentice"))
            elif(self.type == "FQ"):
                self.newCustomerData.append(str("Fully Qualified"))
            
        except(TypeError):
            print("Error - Input data must be the correct data type.")
    
    
    
    def showOptions(self):
        print("#"*40)
        print("Employee Database")
        print("#"*40)
        
        print("1) New Employee")
        return self.askQuestion("Enter a selection ID --> ")

class main:
    def __init__(self):
        self.interface = interface()
        menuSelection = self.interface.showOptions()
        
        if(menuSelection == 1):
            print("Valid!")
            self.addNewCustomer()
            print("You have entered: ");
            print("ID) " + self.interface.newCustomerData[0])
            print("Name) " + self.interface.newCustomerData[1])
            print("Phone) " + self.interface.newCustomerData[2])
            print("Type) " + self.interface.newCustomerData[3])
            
            if(bool(input("Is this info correct? (True/False) "))):
                self.interface.showOptions()
            else:
                self.interface.showNewCustomerForm()
    
    def addNewCustomer(self):
        self.newCustomerData = self.interface.showNewCustomerForm()
            

def initScript():
    print("Loading program ...")
    main()
    
initScript()
    
        
        