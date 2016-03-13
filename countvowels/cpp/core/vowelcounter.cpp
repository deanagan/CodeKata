#include <string>
#include "vowelcounter.h"

VowelCounter::VowelCounter(const std::string inputstr) : m_inputstr(inputstr)
{
}

size_t VowelCounter::Count() const
{
    return std::count_if(m_inputstr.begin(), m_inputstr.end(), CountVowelFunctor());
}


