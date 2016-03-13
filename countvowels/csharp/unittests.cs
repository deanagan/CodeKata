using System;
using System.Text;
using System.Collections.Generic;
using NUnit.Framework;


[TestFixture]
public class OnlyTest
{
    [Test]
    public void MyTest()
    {
        string hello = "hello";
        Assert.AreEqual(VowelCounter.countVowels(ref hello), 2);
    }
}

