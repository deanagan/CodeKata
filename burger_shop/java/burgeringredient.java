public abstract class burgeringredient implements burger {
    protected burger decoratee;
    public abstract String get_ingredients();
    public abstract double get_cost();
    public burgeringredient(burger decoratee) {
        this.decoratee = decoratee;
    }
}
