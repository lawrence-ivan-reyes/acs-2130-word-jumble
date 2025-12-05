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

def solve_final_jumble(letters, final_circles):
    # solves final puzzle where letters get split into multiple words
    # final_circle basically tells us how mnay letters go in each word & returns all possible phrase combos
    # check if number of circles given matches number of letters given
    num_circles = sum(len(circles) for circles in final_circles)
    if num_circles != len(letters):
        print('Number of circles does not match number of letters.')
        return []

    # check if final jumble is just one word, then it's simply one jumble
    num_groups = len(final_circles)
    if num_groups == 1:
        words = solve_one_jumble(letters)
        return [(word,) for word in words]

    # calculate size of each word in final phrase
    group_sizes = [len(circles) for circles in final_circles]
    
    valid_phrases = []
    
    # get all possible words for each position size from dictionary
    # filter words_dict to only include words of the sizes we need
    words_by_size = {}
    for size in set(group_sizes):
        words_by_size[size] = []
        for key, words in words_dict.items():
            if len(key) == size:
                words_by_size[size].extend(words)
    
    # convert letters to a sorted string for comparison
    all_letters_sorted = sorted_letters(letters)
    
    # for a 2-word phrase, try all combos
    if num_groups == 2:
        size1, size2 = group_sizes
        
        # try all combos of letters for the first word
        for combo in itertools.combinations(range(len(letters)), size1):
            # get letters for first word
            first_letters = ''.join(letters[i] for i in combo)
            first_key = sorted_letters(first_letters)
            
            # get remaining letters for second word
            remaining_indices = [i for i in range(len(letters)) if i not in combo]
            second_letters = ''.join(letters[i] for i in remaining_indices)
            second_key = sorted_letters(second_letters)
            
            # check if both keys exist in dictionary
            if first_key in words_dict and second_key in words_dict:
                for word1 in words_dict[first_key]:
                    for word2 in words_dict[second_key]:
                        phrase = (word1, word2)
                        if phrase not in valid_phrases:
                            valid_phrases.append(phrase)
    
    # for 3+ word phrases, use recursive approach
    elif num_groups >= 3:
        valid_phrases = solve_multi_word_jumble(letters, group_sizes)
    
    return valid_phrases

def solve_multi_word_jumble(letters, group_sizes):
    # recursively solve a multi-word jumble
    valid_phrases = []
    
    if len(group_sizes) == 1:
        # base case: just one word left
        words = solve_one_jumble(letters)
        return [(word,) for word in words]
    
    # get size of first word
    first_size = group_sizes[0]
    remaining_sizes = group_sizes[1:]
    
    # try all combos of letters for first word
    for combo in itertools.combinations(range(len(letters)), first_size):
        first_letters = ''.join(letters[i] for i in combo)
        first_key = sorted_letters(first_letters)
        
        if first_key in words_dict:
            # get remaining letters
            remaining_indices = [i for i in range(len(letters)) if i not in combo]
            remaining_letters = ''.join(letters[i] for i in remaining_indices)
            
            # recursively solve the rest
            rest_solutions = solve_multi_word_jumble(remaining_letters, remaining_sizes)
            
            for word1 in words_dict[first_key]:
                for rest in rest_solutions:
                    phrase = (word1,) + rest
                    if phrase not in valid_phrases:
                        valid_phrases.append(phrase)
    
    return valid_phrases

def solve_word_jumble(letters, circles, final):
    # main function that solves the word jumble
    # letters = scrambled words to solve
    # circles = marks which letters from solved words go into final puzzle
    # final = shows how many letters in each word of final answer
    final_letters = ''

    for index in range(len(letters)):
        scrambled_letters = letters[index]
        circled_blanks = circles[index]

        words = solve_one_jumble(scrambled_letters)

        print(f'Jumble {index+1}: {scrambled_letters} => ', end='')
        if len(words) == 0:
            print('(no solution)')
            continue
        print(f'unscrambled into {len(words)} words: {" or ".join(words)}')

        # collect circled letters from first solution
        for letter, blank in zip(words[0], circled_blanks):
            if blank == 'O':
                final_letters += letter

    if len(final_letters) == 0:
        print('Did not solve any jumbles, so could not solve final jumble.')
        return

    final_results = solve_final_jumble(final_letters, final)

    print(f'Final Jumble: {final_letters} => ', end='')
    if len(final_results) == 0:
        print('(no solution)')
        return
    print(f'unscrambled into {len(final_results)} possible phrases:')
    for num, result in enumerate(final_results):
        print(f'    Option {num+1}: {" ".join(result)}')
