export class Sandwitch {
    public ingredients : Set<String> = new Set();

    public listIngredients() : void
    {
        let ingredients_array = [...this.ingredients]
        console.log(`Ingredients: ${ingredients_array.join(', ')}`);
    }
}