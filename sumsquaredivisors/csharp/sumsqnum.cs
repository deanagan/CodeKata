using System;
using System.Collections.Generic;
using System.Linq;

public class SumSquaredDivisors 
{
    public static void Main(string[] args)
    {
    }
		
    public static IEnumerable<long> GetRange(long g, long h)
    {
        long sqrt = (long)Math.Sqrt(h) + 1;
        HashSet<long> yielded = new HashSet<long>();
        for (long e = g; e <= sqrt; ++e)
        {
            if (h % e == 0)
            {
                if (!yielded.Contains(e))
                {
                    yield return e*e;
                    yielded.Add(e);
                }
                long md = h/e;
                if (!yielded.Contains(md))
                {
                    yield return md*md;
                    yielded.Add(md);
                }
            }
        }
    }    
    public static string listSquared(long m, long n)
	{
    string result = "[{0}]";
    List<string> items = new List<string>();
    for (long numbers = m; numbers <= n; ++numbers)
    {
      long sumSquared = GetRange(1, numbers).Sum(ss=>ss);
      
      if (Math.Sqrt(sumSquared) % 1 == 0)
      {
        items.Add(String.Format("[{0}, {1}]", numbers, sumSquared));  
      }
    }
    
    return String.Format(result, String.Join(", ", items));
	}


}



