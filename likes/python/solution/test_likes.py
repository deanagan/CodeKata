import unittest

from likes import likes


class TestLikerMethod(unittest.TestCase):

   def setUp(self):
      self.likers = ['Dean', 'Joshua', 'Cristina', 'Cristuna']

   def test_no_likes_when_list_empty(self):
      self.assertEqual('no one likes this', likes([]))

   def test_like_when_list_has_1(self):
      self.assertEqual('Dean likes this', likes(self.likers[:1]))

   def test_likes_when_list_has_2(self):
      self.assertEqual('Dean and Joshua like this', likes(self.likers[:2]))

   def test_likes_when_list_has_3(self):
      self.assertEqual('Dean, Joshua and Cristina like this', likes(self.likers[:3]))

   def test_likes_when_list_has_more_than_3(self):
      self.assertEqual('Dean, Joshua and 2 others like this', likes(self.likers))



if __name__ == "__main__":
   unittest.main()
