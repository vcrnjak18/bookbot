def main():
	book_path = "books/frankenstein.txt"
	book_text = open_and_read(book_path)
	book_words = word_count(book_text)

	character_dictionary = character_count(book_text)
	pair_list = dict_list(character_dictionary)
	
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{book_words} found in the document\n")

	for pair in pair_list:
		print(f"The '{pair["letter"]}' character was found {pair["count"]} times")

	print("--- End report ---")


def open_and_read(path):
	with open(path) as f:
		content = f.read()
	return content


def word_count(text):
	words = text.split()
	return len(words)


def character_count(text):
	letter_count = {}

	for letter in text:
		lower_letter = letter.lower()
		
		if lower_letter in letter_count:
			letter_count[lower_letter] += 1
		else:
			letter_count[lower_letter] = 1

	return letter_count


def sort_key(dict):
	return dict["count"]

def dict_list(text):
	list_of_pairs = []

	for entry in text:
		empty = {}
		if entry.isalpha():
			empty["letter"] = entry
			empty["count"] = text[entry]
			list_of_pairs.append(empty)
	
	list_of_pairs.sort(reverse=True, key=sort_key)

	return list_of_pairs

main()