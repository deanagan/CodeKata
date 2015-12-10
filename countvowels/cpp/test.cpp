#include <iostream>
#include <cassert>
#include <algorithm>
#include <boost/bind.hpp>

struct CountVowels {
    std::string vowels;
    explicit CountVowels() : vowels("aeiouAEIOU") {
    }

    bool operator()(char ch) 
    {
        return std::find(vowels.begin(), vowels.end(), ch) != vowels.end();
    }

};

int count_vowels(const std::string& inputStr)
{
    return std::count_if(inputStr.begin(), inputStr.end(), CountVowels());
}

int main(void)
{
    std::string inputStr("hello");
    assert(count_vowels(inputStr) == 2);
    std::string vowels("aeiouAEIOU");
    // C++ 11 Style
    std::function<bool (char)> pred = [&](char ch) { return std::find(vowels.begin(), vowels.end(), ch) != vowels.end(); };
    
    int vowelcount = std::count_if(inputStr.begin(), inputStr.end(), pred);
    std::cout << vowelcount << "\n";
}
