import unittest
from piglatin import pig_latin_word, first_vowel_index


class TestPigLatin(unittest.TestCase):

	def test_first_vowel_index(self):
	
		self.assertEqual(first_vowel_index('trashcan') , 2)
		self.assertEqual(first_vowel_index('e') , 0)
		self.assertEqual(first_vowel_index('cry') , False)
		self.assertEqual(first_vowel_index('Creep') , 2)
		self.assertEqual(first_vowel_index('potato') , 1)
		self.assertEqual(first_vowel_index('banana') , 1)
		self.assertEqual(first_vowel_index('crime') , 2)
		
		
	def test_pig_latin_word(self):
	
		self.assertEqual(first_vowel_index('trashcan') , 2)
		self.assertEqual(first_vowel_index('e') , 0)
		self.assertEqual(first_vowel_index('cry') , False)
		self.assertEqual(first_vowel_index('Creep') , 2)
		self.assertEqual(first_vowel_index('potato') , 1)
		self.assertEqual(first_vowel_index('banana') , 1)
		self.assertEqual(first_vowel_index('crime') , 2)
		
		
		
		
		
		
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatin)
	unittest.TextTestRunner(verbosity=2).run(suite)