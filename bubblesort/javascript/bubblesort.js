#!/usr/local/bin/node
var assert = require('assert');
var _ = require('underscore');

function main() {
    assert(_.isEqual(bubblesort([4,3,6,1,7,9,2,5,8]),[1,2,3,4,5,6,7,8,9]), "Not sorted correctly");

}


function bubblesort(tosort) {
    var didSwap = true;

    while (didSwap) {
        didSwap = false;
        for (var i=0; i < tosort.length-1; ++i) {
            if (tosort[i] > tosort[i+1]) {
                // pre es6 swapping else [a,b] = [b,a]
                tosort[i] = tosort[i+1] + (tosort[i+1] = tosort[i], 0);
                didSwap = true;
            }
        }
    }
    
    return tosort;
}



if (require.main === module) {
    main();
}
