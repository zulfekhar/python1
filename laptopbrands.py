from OOPLaptops import laptops


class Macbookpro(laptops):
    def __init__(self):
        laptops.__init__(self)
        print("\nMacbook Pro is the best laptop for Coders")

    def pricerange(self):
        print("Price Range Starting From 80,000 - 2,00,000")    

    def Fingerprint(self):
        print("It Has Fingerprint Feature")

    def batterylife(self):
        print("Battery backup is 8-9 Hours")
    
    def body(self):
        print("Body Is made Up of ALUMINIUM")            


mac = Macbookpro()
mac.pricerange()
mac.sizes()
mac.touchpad()
mac.batterylife()
mac.body()

print('---------------------------')
print('---------------------------')


class Dell(laptops):
    def __init__(self):
        laptops.__init__(self)
        print("Dell is the best laptop for Gamers")

    def camera(self):
        print("It Has Nice camera Quality")

dell = Dell()
dell.pricerange()
dell.sizes()
dell.touchpad()
dell.batterylife()