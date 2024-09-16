import sys

def count_character(content):
    chars_count = {}

    for char in content:
        lower_char = char.lower()
        if lower_char in chars_count:
            chars_count[lower_char] += 1
        else:
            chars_count[lower_char] = 1

    return chars_count

def count_words(content):
    word_lst = content.split()
    return len(word_lst)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_to_arr(chars_dict):
    chars_count = []

    for char, count in chars_dict.items():
        if char.isalpha():
            chars_count.append({
                "char": char,
                "count": count
            })
    
    return chars_count

def sort_by(dict):
    return dict["count"]



def report(book_path):
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_count = convert_to_arr(count_character(text))
    chars_count.sort(reverse=True, key=sort_by)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for char_dict in chars_count:
        char = char_dict["char"]
        count =  char_dict["count"]
        print(f"The '{char}' character was found {count} times")
        
    print(f"--- End report ---")



def main():
    book_path = "books/frankenstein.txt"
    report(book_path)

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit