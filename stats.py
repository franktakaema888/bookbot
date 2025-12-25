def book_word_count(book_text):
  return len(book_text.split())

def book_char_occurrence(book_text):
  char_count = dict()

  for c in book_text:
    lowerCase = c.lower()
    if lowerCase not in char_count:
      char_count[lowerCase] = 1
    else:
      char_count[lowerCase] += 1
  return char_count

def sort_dict(book_dict):
  new_list = []
  for key, value in book_dict.items():
    new_list.append({'name': key, 'num': value})

  new_list.sort(reverse=True, key=sort_on)

  formatted_list = ''

  for d in new_list:
    if d['name'].isalpha():
      formatted_list += '\n' + f"{d['name']}: {d['num']}"
    else:
      continue

  return formatted_list

def sort_on(items):
  return items['num']
