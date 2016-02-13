#pragma once
#include <string>
#include <algorithm>

class VowelCounter {
    
    std::string m_inputstr;


    struct CountVowelFunctor {
        std::string m_vowels;
        explicit CountVowelFunctor() : m_vowels("aeiouAEIOU") { }

        bool operator()(char ch) 
        {
            return std::find(m_vowels.begin(), m_vowels.end(), ch) != m_vowels.end();
        }
    };

public:
    
    explicit VowelCounter(const std::string inputStr);
    size_t Count() const;
};

