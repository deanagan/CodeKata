#!/usr/local/bin/node

//#!/usr/bin/nodejs

function countvowels(inputStr) {
    return inputStr.split("").filter ( function (ch) {
        return ch.search(/[aeiouAEIOU]/) != -1;
    }).length;
}


console.log ("Counting Vowels");

console.log ("The number of vowels in dean is " + countvowels("dean"));

console.log ("The number of vowels in aeiouAEIOU is " + countvowels("aeiouAEIOU"));

console.log ("The number of vowels in bls  is " + countvowels("bls"));

console.log ("The number of vowels in ''  is " + countvowels(""));

console.log ("The number of vowels in super  is " + countvowels("super"));

