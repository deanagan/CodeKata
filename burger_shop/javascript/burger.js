#!/usr/bin/nodejs


function burger() {
    this.ingredients = function() { return "bread buns"; };
    this.cost = function() { return 0.25; };
}

function beef(burger) {
    var ingredients = burger.ingredients();
    burger.ingredients = function() {
        return ingredients + ", beef patty";
    };
    var cost = burger.cost();
    burger.cost = function() {
        return cost + 1.25;
    };
}

function cheese(burger) {
    var ingredients = burger.ingredients();
    burger.ingredients = function() {
        return ingredients + ", cheese"; 
    };
    var cost = burger.cost();
    burger.cost = function() {
        return cost + 0.55;
    };
}


function main() {
    console.log("The Burger Shop");
    var breadOnly = new burger();
    console.log(breadOnly.ingredients()+ " costs " + breadOnly.cost());    
    
    beef(breadOnly);
    
    console.log(breadOnly.ingredients()+ " costs " + breadOnly.cost());    

    cheese(breadOnly);

    console.log(breadOnly.ingredients()+ " costs " + breadOnly.cost());    

}

if (require.main === module) {
    main();
}
