public abstract class Meal {
    public final void doMeal () {
        prepareIngredients ();
        cozinheiro();
        comer();
        Limpar();
    }

    public abstract void prepareIngredients ();

    public abstract void cook ();

    public void eat () {
        System.out.println ("Mmm, isso é bom");
    }

    public abstract void cleanUp ();
}