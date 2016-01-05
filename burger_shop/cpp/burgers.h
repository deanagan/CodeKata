#pragma once


class Burgers {

public:
    virtual ~Burgers() {}
    virtual std::string GetIngredients() const = 0;
    virtual double GetCost() const = 0;

};

class Buns : public Burgers {
    // Make this private to disallow stack allocation 
    ~Buns() {}
public:
    virtual std::string GetIngredients() const { return "Bread buns"; }
    virtual double GetCost() const { return 0.75; }
};

class Ingredients : public Burgers {
    // Disallow copy and assignment of ingredients
    Ingredients(const Ingredients&);
    Ingredients& operator=(const Ingredients&);
protected:
    Burgers* mBurger;
public:
    Ingredients(Burgers* burger) : mBurger(burger) {} 
    virtual ~Ingredients() { if(mBurger) delete mBurger;}
    virtual std::string GetIngredients() const = 0;
    virtual double GetCost() const = 0;
};

class BeefPatty : public Ingredients {
    
public:
    BeefPatty(Burgers* buns) : Ingredients(buns) {}
    virtual ~BeefPatty() {}
    virtual std::string GetIngredients() const { return mBurger->GetIngredients() + ", Beef"; }
    virtual double GetCost() const { return mBurger->GetCost() + 1.25; }

};

class Cheese : public Ingredients {
public:
    Cheese(Burgers* buns) : Ingredients(buns) {}
    virtual ~Cheese() {}
    virtual std::string GetIngredients() const { return mBurger->GetIngredients() + ", Cheese"; }
    virtual double GetCost() const { return mBurger->GetCost() + 1.00; }
};
