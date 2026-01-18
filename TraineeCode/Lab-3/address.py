class Address:
    def __init__(self):
        self._address1 = None
        self._address2 = None
        self._city = None
        self._pincode = None


    @property
    def address1(self):
        return self._address1
    
    @address1.setter
    def address1(self,value):
        self._address1=value
    
    
    
    @property
    def address2(self):
        return self._address2
    
    @address2.setter
    def address2(self,value):
        self._address2=value
    
    
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self,value):
        self._city=value
    

    @property
    def pincode(self):
        return self._pincode
    
    @pincode.setter
    def pincode(self,value):
        self._pincode=value