import itertools

def get_file_lines(filename='/usr/share/dict/words'):
    # reads a file & then returns each line as an uppercase string, stripped of whitespace
    with open(filename) as file:
        lines = [line.strip().upper() for line in file]
    return lines


def sorted_letters(scrambled_letters):
    # takes scrambled letters and sorts them alphabetically
    return ''.join(sorted(scrambled_letters))


def create_words_dict(words_list):
    # creates a dictionary mapping sorted letters to list of words
    words_dict = {}
    for word in words_list:
        # only include words with alphabetic characters
        if word.isalpha():
            key = sorted_letters(word)
        if key not in words_dict:
            words_dict[key] = []
            words_dict[key].append(word)
    return words_dict

def solve_one_jumble(letters):
    # given the scrambled letters, return all valid words they can spell
    # sort letters to create lookup key
    key = sorted_letters(letters)
    
    # look up all words that have the same sorted letters
    if key in words_dict:
        return words_dict[key]
    else:
        return []
