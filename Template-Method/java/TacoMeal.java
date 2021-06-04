public class TacoMeal extends Meal {
    @Sobrepor
    public void prepareIngredients () {
        System.out.println ("Obtendo carne moída e conchas");
    }

    @Sobrepor
    public void cook () {
        System.out.println ("Cozinhar carne moída na panela");
    }

    @Sobrepor
    public void eat () {
        System.out.println ("Os tacos são saborosos");
    }

    @Sobrepor
    public void cleanUp () {
        System.out.println ("Lavando a louça");
    }
}