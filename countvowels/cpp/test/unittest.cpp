#include "vowelcounter.h"
#include "gtest/gtest.h"
#include "gmock/gmock.h"

namespace {


using ::testing::Return;
using ::testing::_;

class MockVowelCounter : public VowelCounter {

    public:

        MockVowelCounter(const std::string inp) : VowelCounter(inp) {}
        MOCK_METHOD0(Count, size_t());

};

TEST(MockingVowelCounter, VowelCount)
{
    MockVowelCounter vcCounter("hello");    
    
    EXPECT_CALL(vcCounter, Count())
//            .WillOnce(Return(2))
            .WillOnce(Return(2));

    EXPECT_EQ(vcCounter.Count(), 2);
}


// The fixture for testing class VowelCount.
class VowelCountTest : public ::testing::Test {
 protected:
  // You can remove any or all of the following functions if its body
  // is empty.

  VowelCountTest() {
    // You can do set-up work for each test here.
  }

  virtual ~VowelCountTest() {
    // You can do clean-up work that doesn't throw exceptions here.
  }

  // If the constructor and destructor are not enough for setting up
  // and cleaning up each test, you can define the following methods:

  virtual void SetUp() {
    // Code here will be called immediately after the constructor (right
    // before each test).
  }

  virtual void TearDown() {
    // Code here will be called immediately after each test (right
    // before the destructor).
  }

  // Objects declared here can be used by all tests in the test case for Foo.
};

// Tests that the counting is correct.
TEST_F(VowelCountTest, MethodCountCorrect) {
  VowelCounter hello("hello");
  EXPECT_EQ(2, hello.Count());
}

// Tests that VowelCounter does Xyz.
TEST_F(VowelCountTest, DoesXyz) {
  // Exercises the Xyz feature of VowelCounter.
}

}  // namespace
/*
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}*/
