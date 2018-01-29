import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('By Ciaran Barnes','Huronreport.com','Sumitomo Life Insurance Company Raised By $468050 Its Union Pac Com (UNP) Holding; Ameritas Investment ...','Sumitomo Life Insurance Company increased Union Pac Corp Com (UNP) stake by 14.38% reported in 2017Q3 SEC fili','"https://huronreport.com/sumitomo-life-insurance-company-raised-by-468050-its-union-pac-com-unp-holding-ameritas-investment-partners-has-upped-ulta-beauty-ulta-position-by-1-72-million/','2018-01-28T10:56:16Z')

    def test_instance(self):
        self.assertTrue(isintance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
