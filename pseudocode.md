## Overview
Main objective: solve word jumble puzzles by unscrambling letters and finding valid dictionary words.

---

## Function: Get File Lines

**Purpose:** Read a dictionary file and prepare the words for processing

**Steps:**
1. Open the dictionary file 
2. For each line in the file:
   - Remove any whitespace from the beginning and end
   - Convert all letters to uppercase
   - Add to a list
3. Return the list of cleaned words

---

## Function: Sorted Letters

**Purpose:** Sort letters alphabetically to create a lookup key

**Steps:**
1. Take the scrambled letters as input
2. Sort all the letters in alphabetical order
3. Join them back into a single string
4. Return the sorted string

**Example:** "ACOME" becomes "ACEMO"

---

## Function: Create Words Dictionary

**Purpose:** Build a dictionary that maps sorted letters to all possible words

**Steps:**
1. Create an empty dictionary
2. For each word in the word list:
   - Check if the word contains only alphabetic characters (no numbers or symbols)
   - Sort the letters in the word alphabetically (this becomes the key)
   - If this sorted key doesn't exist in the dictionary yet, create a new empty list for it
   - Add the original word to the list for this key
3. Return the completed dictionary

**Example:** 
- "DOG" and "GOD" both have sorted letters "DGO"
- Dictionary entry: `"DGO" -> ["DOG", "GOD"]`

---

## Function: Solve One Jumble

**Purpose:** Find all valid words that can be made from scrambled letters

**Steps:**
1. Take the scrambled letters as input
2. Sort the letters alphabetically to create a lookup key
3. Look up this key in the words dictionary
4. If the key exists, return all the words found
5. If the key doesn't exist, return an empty list

---

## Function: Solve Final Jumble

**Purpose:** Solve the final puzzle where letters form multiple words

**Input:**
- Letters to unscramble
- Final circles (shows how many letters go in each word)

**Steps:**

### Initial Validation:
1. Count total number of circles
2. Count total number of letters
3. If they don't match, print error message and return empty list

### Single Word Case:
1. If there's only one group of circles (one word):
   - Treat it as a simple one-word jumble
   - Return all possible words wrapped in tuples

### Two Word Case:
1. Calculate the size of each word from the circle groups
2. Try all possible combinations of splitting the letters:
   - For each combination:
     - Take some letters for the first word
     - Use remaining letters for the second word
     - Sort both sets of letters
     - Look up both in the dictionary
     - If both exist, save all word combinations as valid phrases
3. Return all valid phrase combinations

### Three or More Words:
1. Call the multi-word jumble solver function
2. Return the results

---

## Function: Solve Multi-Word Jumble

**Purpose:** Recursively solve jumbles with 3 or more words

**Steps:**

### Base Case (One Word Left):
1. If only one word size remains:
   - Solve it as a simple jumble
   - Return each word wrapped in a tuple

### Recursive Case (Multiple Words):
1. Get the size of the first word
2. Get the sizes of all remaining words
3. Try all possible combinations for the first word:
   - For each combination:
     - Extract those letters for the first word
     - Sort them and look up in dictionary
     - If valid words exist:
       - Get the remaining letters
       - Recursively solve the remaining words
       - Combine each first word with each solution from the rest
       - Add to valid phrases list
4. Return all valid phrases found

---

## Function: Solve Word Jumble (Main Function)

**Purpose:** Solve the complete word jumble puzzle from start to finish

**Input:**
- Letters: list of scrambled words
- Circles: marks which letters go into the final puzzle (O = circled, _ = not circled)
- Final: shows structure of final answer

**Steps:**

### Part 1: Solve Individual Jumbles
1. Create an empty string to collect final letters
2. For each scrambled word:
   - Print which jumble we're solving
   - Find all possible unscrambled words
   - If no solution found, print message and continue to next
   - If solutions found, print them all
   - Look at the circles pattern and the first solution:
     - For each position marked with 'O', take that letter
     - Add these circled letters to the final letters string

### Part 2: Solve Final Jumble
1. If no final letters were collected:
   - Print error message and stop
2. Otherwise:
   - Use the collected letters to solve the final jumble
   - Print how many possible phrase solutions were found
   - Print each phrase option, numbered and formatted nicely

---

## Test Cases

### Test 1: Single-word final answer
- Solve 4 scrambled words
- Extract circled letters
- Final answer is one 7-letter word

### Test 2: Two-word final answer
- Solve 4 scrambled words
- Extract circled letters  
- Final answer is two words (4 letters and 3 letters)

### Test 3: Two-word final answer
- Solve 4 scrambled words
- Extract circled letters
- Final answer is two words (5 letters and 5 letters)

### Test 4: Two-word final answer with theme
- Cartoon prompt about why Farley rolled on the barn floor
- Final answer is two words (2 letters and 6 letters)

---

## Main Program Flow

1. Read all words from the dictionary file
2. Build the sorted-letters dictionary for fast lookups
3. Show some example lookups to verify the dictionary works
4. Run all four test cases to demonstrate the solver
