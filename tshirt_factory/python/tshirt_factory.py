#!/usr/bin/python3
from abc import ABCMeta, abstractmethod
from random import choice


class Tshirt(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):

        self.brand = "Generic"
        self.cotton = 50
        self.polyester = 50
        self.mfg = "China"

    def print_tag(self):
        print("{0} Cotton {1}% Polyester {2}%. Made in {3}".format(self.brand, self.cotton, self.polyester, self.mfg))

class UniqloTshirt(Tshirt):
    def __init__(self):
        self.brand = "uniqlo"
        self.cotton = 80
        self.polyester = 20
        self.mfg = "Japan"

        
class GiordanoTshirt(Tshirt):
    def __init__(self):
        self.brand = "giordano"
        self.cotton = 70
        self.polyester = 30
        self.mfg = "Hong Kong"

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

class Factory(metaclass=Singleton):
    def __init__(self):
        tag = choice(range(2))
        if tag == 0:
            self.cls = UniqloTshirt()
        else:
            self.cls = GiordanoTshirt()

    def get_tshirt(self):
        return self.cls

if __name__ == "__main__":
    print("The tshirt factory!\n")

    tshirt = Factory()
    tee = tshirt.get_tshirt().print_tag()

    same_tshirt = Factory()

#    print(tshirt is same_tshirt)
    
    #try:
    #badtee = Tshirt()
    #badtee.print_tag()
    #except:
    #    print("Not allowed")
