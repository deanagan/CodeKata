#include <iostream>
#include <cassert>
#include <algorithm>
#include <boost/bind.hpp>
#include "vowelcounter.h"


int main(void)
{
    std::string inputStr("hello");

    VowelCounter vowelcounter("hello");
    assert(vowelcounter.Count() == 2);
    

    // C++ 11 Style
    std::string vowels("aeiouAEIOU");
    std::function<bool (char)> pred = [&](char ch) { return std::find(vowels.begin(), vowels.end(), ch) != vowels.end(); };
    
    int vowelcount = std::count_if(inputStr.begin(), inputStr.end(), pred);
    std::cout << vowelcount << "\n";
}
