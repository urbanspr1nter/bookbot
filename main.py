path_to_file = "books/frankenstein.txt"

def count_words(data):
    words = data.split()
    word_count = len(words)

    return word_count


def count_letters(data):
    letter_dict = {}
    lowered_data = data.lower()
    for letter in lowered_data:
        if letter.isalpha() == False:
            continue
        
        if letter not in letter_dict:
            letter_dict[letter] = 0

        letter_dict[letter] += 1

    return letter_dict


def dict_to_list(letter_dict):
    result = []
    for letter in letter_dict:
        result.append({"letter": letter, "count": letter_dict[letter]})

    return result


def print_report(data):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(data)} words")
    print()
    
    letter_count_list = dict_to_list(count_letters(data))
    letter_count_list.sort(key=lambda x: x["count"], reverse=True)
    for letter in letter_count_list:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")

    print(f"--- End report ---")


def main():
    with open(path_to_file) as f:
        file_contents = f.read()

        print_report(file_contents)


main()

