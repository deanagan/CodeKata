using System;
using System.Text;
using System.Collections.Generic;
using NUnit.Framework;


[TestFixture]
public class OnlyTest
{
    [Test]
    public void MyTest1()
    {
        
        Assert.AreEqual(true, Solution.IsVampire(21, 6));
    }

    [Test]
    public void MyTest2()
    {
        Assert.AreEqual(true, Solution.IsVampire(204, 615));
    }    

    [Test]
    public void MyTest3()
    {
        Assert.AreEqual(true, Solution.IsVampire(30, -51));
    }   

    [Test]
    public void MyTest4()
    {
        Assert.AreEqual(false, Solution.IsVampire(-246, -510));
    }    

    [Test]
    public void MyTest5()
    {
        Assert.AreEqual(true, Solution.IsVampire(210, 600));
    }
}

