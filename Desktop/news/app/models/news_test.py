import unittest
from news import News


class NewsTest(unittest.TestCase):


  def setUp(self):

      self.new_news = News('Daniel Kuhn','bitcoin','As Museums Go Dark',"With the physical world closed",
      "https://www.coindesk.com/as-museums-go-dark-crypto-art-finds-its-frame",
      "https://www.coindesk.com/wp-content/uploads/2020/04/Coldie-Julian-Assange-Decentral-Eyes-Gold-Edition-1_1-1200x628.jpg",
      "2020-04-22T18:49:06Z",'With the lights turned off')

   

  def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
       
    


if __name__ == '__main__':
    unittest.main()