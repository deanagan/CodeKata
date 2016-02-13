#include <locale>
#include <iostream> // cout
#include <iomanip> //set precision
#include <boost/shared_ptr.hpp>
#include <sstream>

class comma_numpunct : public std::numpunct<char>
{
  protected:
    virtual char do_thousands_sep() const
    {
        return ',';
    }

    virtual std::string do_grouping() const
    {
        return "\3";
    }
};

int main()
{
    std::locale comma_locale(std::locale(), new comma_numpunct);
    std::stringstream ss;
    
    // tell ss to use our new locale.
    ss.imbue(comma_locale);
    ss << std::setprecision(2) << std::fixed << 1000000.1234 << "\n";
    
    // reset locale
    ss.imbue(std::locale("C"));
    ss << 1000;
    std::cout << ss.str() << "\n";
}
