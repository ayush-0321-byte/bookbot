from stats import get_num_words, get_char_count, report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(get_book_text(sys.argv[1]))
    dic_char = (get_char_count(get_book_text(sys.argv[1])))
    ret = []

    for key in dic_char:
        t = {}
        if key.isalpha():
            t["char"] = key
            t["num"] = dic_char[key]
            ret.append(t)
    ans = report(ret)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for a in ans:
        print(f"{a["char"]}: {a["num"]}")
    print("============= END ===============")



main()