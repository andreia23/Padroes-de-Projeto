import {SandwitchBuilder} from './Builder';
import { Sandwitch } from './Sandwitch';

export class ConcreteBuilder implements SandwitchBuilder
{
    private sandwitch;

    constructor()
    {
        this.sandwitch = new Sandwitch();
    }

    addLettuce(): void {
        this.sandwitch.ingredients.add('lettuce');
    }
    addChicken(): void {
        this.sandwitch.ingredients.add('chicken');
    }
    addBacon(): void {
        this.sandwitch.ingredients.add('bacon');
    }
    addTomato(): void {
        this.sandwitch.ingredients.add('tomato');
    }
    addCheese(): void {
        this.sandwitch.ingredients.add('cheese');
    }
    addHam(): void {
        this.sandwitch.ingredients.add('ham');
    }

    public getSandwitch() : Sandwitch
    {
        const result = this.sandwitch;
        this.sandwitch = new Sandwitch();
        return result;
    }
    
}