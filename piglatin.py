import sys
import os


def first_vowel_index(word):

	"""
	This function returns the index of the first vowel in a word
	
	
	e.g. first_vowel_index('trash') = 2
	
	"""

	word = word.lower()

	vowel_list = ["a", "e", "i", "o", "u"]

	for index in range(len(word)):
	
		if word[index] in vowel_list:
		
			return index
			
	return False


def strip_punctuation(word):

	"""
	This function strips the punctation from the beginning and end of the word.
	
	It returns a list containing the front and end punctuation as well as the stripped word.

	Also does the same for numeric characters.
	"""

	punctuation_list = [".", ",", "?", "!",";", ":", "'", '"', "(", ")", "<", ">", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "“", "”"]

	punctuation = []
	
	front_punctuation = ""
	
	end_punctuation = ""
	
	
	for char in word: #front punctuation
	
		if char not in punctuation_list:
		
			break
			
		else:
		
			front_punctuation = front_punctuation+char
			
					
	for char in reversed(word): #end punctuation
	
		if char not in punctuation_list:
		
			break
			
		else:
		
			end_punctuation = end_punctuation+char
			
	#strip punctuation from the word		
	no_punctuation_word = word[len(front_punctuation):len(word)-len(end_punctuation)]
			
	end_punctuation = end_punctuation[::-1] #reverse end punctuation
			
	return [front_punctuation, end_punctuation, no_punctuation_word]
	
	



def pig_latin_word(word):

	"""
	This function converts a word to pig patin.
	
	The function will ensure punctuation marks remain at the end of the word.
	
	The function will only recognise capital letters at the beginning of the word. The
	first letter of the new word will also be a capital in this case.
	
	"""
	
	
	if is_valid_word(word) ==False:
	
		return word
		

	vowel_list = ["a", "e", "i", "o", "u"]	
	capital_flag = False
	word_length = len(word)
	punctuation_list = strip_punctuation(word)
	

	front_punctuation = punctuation_list[0]
	end_punctuation = punctuation_list[1]
	word = punctuation_list[2]	
	
		
	if word[0].isupper() == True: 
	
		capital_flag = True
	
	if word[0].lower() in vowel_list: #if the word begins with a vowel
	
		word = word + "way"

	else:
	
		first_vowel = first_vowel_index(word)
		
		word = word[first_vowel:] + word [:first_vowel] + "ay"
		
		word = word.lower()
	
		
		if capital_flag == True:
		
			first_letter = word[0]
			first_letter = first_letter.upper()
			word = first_letter + word[1:]
			
	return front_punctuation + word + end_punctuation
	
	
	
def pig_latin_sentence(sentence):

	"""
	Runs the pig_latin_word function on each word in a sentence.
	
	Returns a string of the pig latin sentence.
	
	Each word in the original is separated by a single space
	"""
		
	#sentence = sentence.rstrip() #get rid of newline characters etc.
		
	new_string = ""

	word_list = sentence.split()
	

	for word in word_list:

		new_string = new_string+ pig_latin_word(word) + " "
		
	return new_string[:len(new_string)-1] #cut off final space

def is_valid_word(word):

	"""
	Checks that word contains at least one alphabetical character.
	
	"""

	for char in word:
	
		if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
		
			return True

	else:
	
		return False

	
def main():
	


	try:

		input_file = open(sys.argv[1], "r")
		
		
	except:
	
		print ("Error : No file with that name found")
		return
	
	assert sys.argv[1][len(sys.argv[1])-4:] == ".txt", "Error: Please enter a .txt file as input"

	if os.path.isfile(sys.argv[2]) == True:
	
		print ("Error: There is already a file with that name.")
		return
	
	output_file = open(sys.argv[2], "w")
	
	for line in input_file:
	
		sentence = pig_latin_sentence(line)
		
		output_file.write(sentence + "\n")
		
		

	
	
if __name__ == '__main__':

	main()
	
	
	
	
	
	
	
	
	
	

	
	
	