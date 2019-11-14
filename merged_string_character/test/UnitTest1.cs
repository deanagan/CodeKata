using NUnit.Framework;
using solution;

namespace test
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {
            Assert.IsTrue(StringMerger.isMerge("codewars", "code", "wars"), "codewars can be created from code and wars");
        }

        //[Test]
        // public void HappyPath2()
        // {
        //     Assert.IsTrue(StringMerger.isMerge("codewars", "cdwr", "oeas"), "codewars can be created from cdwr and oeas");
        // }

        // [Test]
        // public void SadPath1()
        // {
        //     Assert.IsFalse(StringMerger.isMerge("codewars", "cod", "wars"), "Codewars are not codwars");
        // }

        // [Test]
        // public void Bananas()
        // {
        //     Assert.IsTrue(StringMerger.isMerge("Bananas from Bahamas", "Bahas", "Bananas from am"), "Going Bananas!");
        // }
    }
}