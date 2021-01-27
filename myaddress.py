class Address:
    def __init__(self,name,phone,address):
        super().__init__(name,phone)
        self.address=address

    def getAddressInfo(self):
        super().getCustomerInfo()
        print('Address Details')
        print(self.address)
