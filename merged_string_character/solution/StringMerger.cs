using System;
using System.Linq;
using System.Collections.Generic;

namespace solution
{
    public class StringMerger
    {
        public static bool isMerge(string s, string part1, string part2)
        {
            var q1 = new Queue<char>(part1);
            var q2 = new Queue<char>(part2);
            var input = new Queue<char>(s);
            
            while (input.Any())
            {
                int q1match = 0;
                int q2match = 0;
                if (q1.Any())
                {
                    q1match = input.Zip(q1, (q1e,ie) => (q1e, ie))
                                   .TakeWhile((ch) => ch.ie ==ch.q1e)
                                   .Count((c)=>true);
                }
                if (q2.Any())
                {
                    q2match = input.Zip(q2, (q2e,ie) => (q2e, ie))
                                   .TakeWhile((ch) => ch.ie ==ch.q2e)
                                   .Count((c)=>true);
                }
                Console.WriteLine($"{q1match} {q2match}");
                if (q1match >= q2match)
                {
                    if (input.ToArray().Length < q1match)
                    {
                        return false;
                    }
                    Console.WriteLine($"{q1match} to dequeue from q1 {q1.ToArray().Length} size");
                    Console.WriteLine($"{q1match} to dequeue from input {input.ToArray().Length} size");
                    for(var i = 0; i < q1match; q1match++)
                    {
                        q1.Dequeue();
                        input.Dequeue();
                    }
                    
                }
                else
                {
                    if (input.ToArray().Length < q2match)
                    {
                        return false;
                    }
                    for(var i = 0; i < q2match; q2match++)
                    {
                        q2.Dequeue();
                        input.Dequeue();
                    }
                }
                                   
            }
            return !(q1.Any() || q2.Any());
        }

    }
}
