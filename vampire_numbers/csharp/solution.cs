using System;
using System.Linq;

class Solution 
{

    public static void Main(string[] args) 
    {
        Console.WriteLine("Hello!");
        Console.WriteLine(IsVampire(21,6));
    }

    public static bool IsVampire(int x, int y)
    {

        return (x*y).ToString().ToCharArray().OrderBy(ch=>ch).SequenceEqual( (x.ToString() + y.ToString()).ToCharArray().OrderBy(ch=>ch) );
    }
}
