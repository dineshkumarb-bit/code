class Customer:
    def __init__(self,cname,cphone):
        self.name=cname
        self.phone=cphone

    def getCustomerInfo(self):
        print("Customer Details")
        print(self.name,self.phone)
