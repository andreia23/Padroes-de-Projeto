import { ConcreteBuilder } from "./ConcreteBuilder";

const sandwitchbuilder = new ConcreteBuilder();
sandwitchbuilder.addBacon();
sandwitchbuilder.addLettuce();
sandwitchbuilder.addTomato();

let sandwitch = sandwitchbuilder.getSandwitch();

console.log('BLT: ');
sandwitch.listIngredients();

//

sandwitchbuilder.addCheese();
sandwitchbuilder.addHam();

sandwitch = sandwitchbuilder.getSandwitch();

console.log('Misto:');
sandwitch.listIngredients();