from stats import book_word_count, book_char_occurrence, sort_dict
import sys

def main():
  print(sys.argv)
  print("Usage: python3 main.py <path_to_book>")
  # sys.exit(1)
  
  book_list = get_book_text(sys.argv[1])
  num_words = book_word_count(book_list)
  # print(f'Found {num_words} total words')

  book_dict = book_char_occurrence(book_list)
  # print(book_dict)

  sorted_dict = sort_dict(book_dict)

  formatted_output = f"""
  ============ BOOKBOT ============
  Analyzing book found at books/frankenstein.txt...
  ----------- Word Count ----------
  Found {num_words} total words
  --------- Character Count -------
  {sorted_dict}
  """
  print(formatted_output)



def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

main()