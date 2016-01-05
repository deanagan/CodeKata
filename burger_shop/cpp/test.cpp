#include <iostream>

#include "burgers.h"

int main()
{
    Burgers* bunsOnly = new Buns;
    std::cout << "I have " << bunsOnly->GetIngredients() << " and it costs " << bunsOnly->GetCost() << "$\n";
    delete bunsOnly;

    Burgers* hamburger = new BeefPatty(new Buns);
    std::cout << "I have " << hamburger->GetIngredients() << " and it costs " << hamburger->GetCost() << "$\n";
    delete hamburger;

    Burgers* cheeseburger = new Cheese(new BeefPatty(new Buns));
    std::cout << "I have " << cheeseburger->GetIngredients() << " and it costs " << cheeseburger->GetCost() << "$\n";
    delete cheeseburger;

}
