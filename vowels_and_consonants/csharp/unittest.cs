using System;
using NUnit.Framework;
using System.Linq;

[TestFixture]
public class Tests
{
  [Test]
  public static void FixedTest()
  {
    Counter re = Kata.GetCount("Test");
    Assert.AreEqual(1, re.Vowels);
    Assert.AreEqual(3, re.Consonants);
    
    re = Kata.GetCount("Here is some text!");
    Assert.AreEqual(6, re.Vowels);
    Assert.AreEqual(8, re.Consonants);
    
    re = Kata.GetCount("To be a Codewarrior or not to be");
    Assert.AreEqual(12, re.Vowels);
    Assert.AreEqual(13, re.Consonants);
    
    re = Kata.GetCount("To Kata or not to Kata");
    Assert.AreEqual(8, re.Vowels);
    Assert.AreEqual(9, re.Consonants);
    
    re = Kata.GetCount("aeiou");
    Assert.AreEqual(5, re.Vowels);
    Assert.AreEqual(0, re.Consonants);
  }
}
