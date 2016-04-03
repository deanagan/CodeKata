using System;
using System.Linq;


public class Kata
{
 public class Counter {
    public int Vowels {get;set;}
    public int Consonants {get;set;}

}
 
  public static void Main(string[] args)
  {
  }
  public static Counter GetCount(object word)
  {
    Counter c = new Counter();
    c.Vowels = 0;
    c.Consonants = 0;
    if (word is string)
    {
    }
    return c;        
  }
}


