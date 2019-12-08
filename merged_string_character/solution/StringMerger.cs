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
            var duplicates = new Queue<char>();

            while(input.Any())
            {
                var matchCount = 0;
                if (q1.Any() && q1.Peek() == input.Peek())
                {
                    q1.Dequeue();
                    matchCount++;
                }

                if (q2.Any() && q2.Peek() == input.Peek())
                {
                    if (matchCount > 0)
                    {
                        duplicates.Enqueue(q2.Dequeue());
                    }
                    else
                    {
                        q2.Dequeue();
                    }
                    matchCount++;
                }

                if (matchCount > 0)
                {
                    input.Dequeue();
                }
                else
                {
                    if (duplicates.Any() && input.Peek() == duplicates.Peek())
                    {
                        input.Dequeue();
                        duplicates.Dequeue();
                    }
                    else
                    {
                        return false;
                    }
                }

            }
            return !(q1.Any() || q2.Any());
        }

    }
}
