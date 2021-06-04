public class HamburgerMeal extends Meal {
    @Sobrepor
    public void prepareIngredients () {
        System.out.println ("Obtendo hambúrgueres, pães e batatas fritas");
    }

    @Sobrepor
    public void cook () {
        System.out.println ("Cozinhar hambúrgueres na grelha e batatas fritas no forno");
    }

    @Sobrepor
    public void cleanUp () {
        System.out.println ("Jogando fora pratos de papel");
    }
}