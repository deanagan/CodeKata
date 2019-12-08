import unittest

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self._collection_size = len(collection)

    self._pages = {}
    self._total_pages = len(collection)//items_per_page + 1 if len(collection)%items_per_page else 0
    for i in range(self._total_pages):
      start = i*items_per_page
      end = start + items_per_page
      self._pages.setdefault(i, []).extend(collection[start:end])


  # returns the number of items within the entire collection
  def item_count(self):
    return self._collection_size

  # returns the number of pages
  def page_count(self):
    return self._total_pages

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    if page_index not in self._pages:
      return -1
    return len(self._pages[page_index])

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    if item_index < 0 or item_index >= self._collection_size:
      return -1
    for k,v in self._pages.items():
      if item_index + 1 in v:
        return k
    return -1

class TestPaginationHelper(unittest.TestCase):  
  def setUp(self):
    collection = range(1,25)
    self._helper = PaginationHelper(collection, 10)
    
  def test_page_count_is_correct(self):
    self.assertEqual(self._helper.page_count(), 3, 'page_count is returning incorrect value.')

  def test_item_count_is_correct(self):
    self.assertEquals(self._helper.item_count(), 24, 'item_count returned incorrect value')

  def test_page_index_is_correct(self):
    self.assertEquals(self._helper.page_index(23), 2, 'page_index returned incorrect value')

  def test_page_index_is_correct_where_index_is_zero(self):
    self.assertEquals(self._helper.page_index(0), 0, 'page_index returned incorrect value')


if __name__ == '__main__':
    unittest.main()

