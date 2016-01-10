#!/usr/bin/python3

class Buns(object):
    def __init__(self):
        self.ingredients = "Bread buns"
        self.cost = 0.25
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_cost(self):
        return self.cost


class Beef(object):
    def __init__(self, _wrappee):
        self._wrappee = _wrappee
    
    def get_ingredients(self):
        return self._wrappee.get_ingredients() + ", beef"
    
    def get_cost(self):
        return self._wrappee.get_cost() + 1.25


class Cheese(object):
    def __init__(self, _wrappee):
        self._wrappee = _wrappee
    
    def get_ingredients(self):
        return self._wrappee.get_ingredients() + ", cheese"

    def get_cost(self):
        return self._wrappee.get_cost() + 0.75

if __name__ == "__main__":
    bunOnly = Buns()
    print(bunOnly.get_ingredients(), bunOnly.get_cost())

    hamburger = Beef(Buns())
    print(hamburger.get_ingredients(), hamburger.get_cost())

    cheeseburger = Cheese(Beef(Buns()))
    print(cheeseburger.get_ingredients(), cheeseburger.get_cost())    
