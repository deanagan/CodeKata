import java.util.*;



class burgershop {
    public static void main(String[] args) {
        System.out.println("The Burger Shop - Java style!");
        burger bunsOnly = new bun();
        System.out.println(String.format("Buns Only:\nIngredients: %s\nCost:%.2f", bunsOnly.get_ingredients(), bunsOnly.get_cost()));

        burger hamBurger = new patty(new bun());
        System.out.println(String.format("Hamburger:\nIngredients: %s\nCost:%.2f", hamBurger.get_ingredients(), hamBurger.get_cost()));
    }
}


