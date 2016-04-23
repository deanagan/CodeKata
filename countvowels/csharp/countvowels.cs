using System;
using System.Linq;


class VowelCounter {

    public static int countVowels ( string args )
    {
        return args.ToList().Count(ch => "aeiouAEIOU".IndexOf(ch) != -1);
    }

    public static void Main(string[] args)
    {
        string inputStr = "hello";
        Console.WriteLine("Counting the vowels in hello: " + countVowels(inputStr));

    }


}
