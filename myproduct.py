from multiple.myaddress import Address
from multiple.mycustomer import Customer
class Product(Address,Customer):
   def __init__(self,name,phone,address,pname):
       super().__init__(name,phone,address)
       self.pname=pname

   def getProductInfo(self):
       super().getAddressInfo()
       print("Product details")
       print(self.pname)

p=Product('Ram',9876543212,'Bangalore','Iphone')
p.getProductInfo()
