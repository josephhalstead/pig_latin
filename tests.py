import unittest
from piglatin import pig_latin_word, first_vowel_index, pig_latin_sentence, strip_punctuation


class TestPigLatin(unittest.TestCase):

	def test_first_vowel_index(self):
	
		self.assertEqual(first_vowel_index('trashcan') , 2)
		self.assertEqual(first_vowel_index('e') , 0)
		self.assertEqual(first_vowel_index('cry') , False)
		self.assertEqual(first_vowel_index('Creep') , 2)
		self.assertEqual(first_vowel_index('potato') , 1)
		self.assertEqual(first_vowel_index('banana') , 1)
		self.assertEqual(first_vowel_index('crime') , 2)
		self.assertEqual(first_vowel_index('the') , 2)
		
		
	def test_pig_latin_word(self):
	
		self.assertEqual(pig_latin_word('.pig') , '.igpay')
		self.assertEqual(pig_latin_word('"banana') , '"ananabay')
		self.assertEqual(pig_latin_word('trash') , 'ashtray')
		self.assertEqual(pig_latin_word('!happy!!') , '!appyhay!!')
		self.assertEqual(pig_latin_word('duck') , 'uckday')
		self.assertEqual(pig_latin_word('glove') , 'oveglay')
		self.assertEqual(pig_latin_word('eat') , 'eatway')
		self.assertEqual(pig_latin_word('are"') , 'areway"')
		self.assertEqual(pig_latin_word("the'") , "ethay'")
		self.assertEqual(pig_latin_word("I'") , "Iway'")
		self.assertEqual(pig_latin_word('"I') , '"Iway')
		
			
		self.assertEqual(pig_latin_word('Pig') , 'Igpay')
		self.assertEqual(pig_latin_word('??Banana!!') , '??Ananabay!!')
		self.assertEqual(pig_latin_word('trash!') , 'ashtray!')
		self.assertEqual(pig_latin_word('happy?') , 'appyhay?')
		self.assertEqual(pig_latin_word('Duck.') , 'Uckday.')
		self.assertEqual(pig_latin_word('glove:') , 'oveglay:')
		self.assertEqual(pig_latin_word('Eat') , 'Eatway')
		self.assertEqual(pig_latin_word('Are,') , 'Areway,')
		self.assertEqual(pig_latin_word('Welcome,') , 'Elcomeway,')
		self.assertEqual(pig_latin_word('e,') , 'eway,')
		self.assertEqual(pig_latin_word(',') , ',')
		self.assertEqual(pig_latin_word('2009') , '2009')
		self.assertEqual(pig_latin_word('e2009') , 'eway2009')

	def test_pig_latin_sentence(self):
		
		self.assertEqual(pig_latin_sentence("The quick brown fox jumped over the 'lazy dog'!") , "Ethay uickqay ownbray oxfay umpedjay overway ethay 'azylay ogday'!")
		
		
		
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatin)
	unittest.TextTestRunner(verbosity=2).run(suite)