using System.Linq;

namespace Solution
{
  public static class SpacesRemover
  {
    public static string NoSpace(string input)
    {
        return string.Concat(from ch in input
                where ch != ' '
                select ch);
    }
  }
}
