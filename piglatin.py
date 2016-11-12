import sys


mystring = "Peter Carter, chief executive of the Royal College of Nursing, said"

splitlist = mystring.split()


def first_vowel_index(word):

	"""
	This function returns the index of the first vowel in a word
	
	
	e.g. first_vowel_index('trash') = 2
	
	"""

	word = word.lower()

	vowel_list = ["a", "e", "i", "o", "u"]

	for index in range(len(word)-1):
	
		if word[index] in vowel_list:
		
			return index
			
	return False


def pig_latin_word(word):

	"""
	This function converts a word to pig patin.
	
	The function will ensure punctuation marks remain at the end of the word.
	
	The function will only recognise capital letters at the beginning of the word. The
	first letter of the new word will also be a capital in this case.
	
	"""

	vowel_list = ["a", "e", "i", "o", "u"]

	punctuation_list = [".", ",", "?", "!",";", ":"]
	
	capital_flag = False
	punctuation_holder = ""
	word_length = len(word)
	
	if word[word_length-1] in punctuation_list:  #if the last character is a punctuation mark
	
		punctuation_holder = word[word_length-1] #store the punctuation mark in a variable
		
		word=word[0:word_length-1] #cut the punctuation mark off the end of the word
		
		
	if word[0].isupper() == True: 
	
		capital_flag = True
	
	if word[0].lower() in vowel_list: #if the word begins with a vowel
	
		word = word + "way" + punctuation_holder 

	else:
	
		first_vowel = first_vowel_index(word)
		
		word = word[first_vowel:] + word [:first_vowel] + "ay" + punctuation_holder
	
		
		if capital_flag == True:
		
			first_letter = word[0]
			first_letter = first_letter.upper()
			word = first_letter + word[1:]
			
	return word


def main():

	user_string = 'Do you like cheese and making trash potatoes!'
	
	new_string = ""
	
	
	word_list = user_string.split()
	
	for word in word_list:
	
		new_string = new_string + pig_latin_word(word) + " "
		
	print (new_string)
	
	

	
if __name__ == '__main__':
	main()
	
	
	
	
	
	
	