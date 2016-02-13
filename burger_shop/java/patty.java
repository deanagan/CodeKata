


public class patty extends burgeringredient {
    public patty(burger decoratee) {
        super(decoratee);
    }
    @Override
    public String get_ingredients() {
        return this.decoratee.get_ingredients() + ", burger patty";
    }
    @Override
    public double get_cost() {
        return this.decoratee.get_cost() + 1.75;
    }

}
