public class SumSquaredDivisors 
{
		
	public static string listSquared(long m, long n)
	{
    string result = "[{0}]";
    List<string> items = new List<string>();
		for (long numbers = m; numbers <= n; ++numbers)
    {
      long sumSquared = Enumerable.Range(1, numbers)
                                  .Where(divisor=> numbers%divisor == 0)
                                  .Select(sqnum=>sqnum*sqnum).Sum(ss=>ss);
      
      if (Math.Sqrt(sumSquared) % 1 == 0)
      {
        items.Add(String.Format("[{0}, {1}]", numbers, sumSquared);  
      }
    }
    
    return String.Join(", ", items);
	}
}

