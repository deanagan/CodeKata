using System;

namespace FastfoodChain {

public class BurgerShop {

    public static void Main(string[] args)
    {
        Console.WriteLine("This is a decorator example");

        IBurger burgerBread = new BurgerBuns();

        Console.WriteLine(String.Format("I have {0}", burgerBread.GetBurgerDescription()));
        Console.WriteLine(String.Format("It costs {0:C2}$", burgerBread.GetBurgerCost()));

        IBurger cheeseburger = new BeefPatty(new Cheese(new BurgerBuns()));

        Console.WriteLine(String.Format("I have {0}", cheeseburger.GetBurgerDescription()));
        Console.WriteLine(String.Format("It costs {0:C2}$", cheeseburger.GetBurgerCost()));

        IBurger hamburger = new BeefPatty(new BurgerBuns());

        Console.WriteLine(String.Format("I have {0}", hamburger.GetBurgerDescription()));
        Console.WriteLine(String.Format("It costs {0:C2}$", hamburger.GetBurgerCost()));

 
    }
}

public interface IBurger {
    string GetBurgerDescription();
    double GetBurgerCost();
}

public class BurgerBuns : IBurger {


    public string GetBurgerDescription()
    {
        return "Burger buns";
    }

    public double GetBurgerCost()
    {
        return 1.25;
    }
}

public abstract class BurgerIngredients : IBurger {
    // Our burger to embellish
    protected IBurger burger;
    
    public BurgerIngredients(IBurger burger)
    {
        this.burger = burger;
    }

    public virtual string GetBurgerDescription()
    {
        return burger.GetBurgerDescription();
    }
    
    public virtual double GetBurgerCost()
    {
        return burger.GetBurgerCost();
    }
}

public class BeefPatty : BurgerIngredients
{
    public BeefPatty(IBurger burger) : base(burger) 
    {
    }

    public override string GetBurgerDescription()
    {
        return burger.GetBurgerDescription() + " with beef patty,";
    }

    public override double GetBurgerCost()
    {
        return burger.GetBurgerCost() + 3.50;
    }
}

public class Cheese : BurgerIngredients
{
    public Cheese(IBurger burger) : base(burger)
    {}

    public override string GetBurgerDescription()
    {
        return burger.GetBurgerDescription() + " with cheese,";
    }

    public override double GetBurgerCost()
    {
        return burger.GetBurgerCost() + 0.75;
    }
}

}
