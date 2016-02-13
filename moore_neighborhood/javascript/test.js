#!/usr/local/bin/node

var assert = require('assert');

var count_neighbours = function(grid, row, col) {

    return 3;
}

var main = function() {
    assert (count_neighbours([[1, 0, 0, 1, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 1],
                             [1, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0]], 1, 2) === 3, "1st example");
    /*
    assert (count_neighbours([[1, 0, 0, 1, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 1],
                             [1, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0]], 0, 0) === 1, "2nd example");

    assert (count_neighbours([[1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]], 0, 2) === 3, "Dense corner");

    assert (count_neighbours([[0, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0]], 1, 1) === 0, "Single");
    */
}

if (require.main === module) {
    main();
}

  
