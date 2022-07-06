"""Reference: https://en.wikipedia.org/wiki/Soundex#American_Soundex
American Soundex:
The Soundex code for a name consists of a letter followed by three numerical 
digits: the letter is the first letter of the name, and the digits encode the 
remaining consonants. Consonants at a similar place of articulation share the 
same digit so, for example, the labial consonants B, F, P, and V are each 
encoded as the number 1. The correct value can be found as follows:
1. Retain the first letter of the name and drop all other occurrences 
of a, e, i, o, u, y, h, w.
2. Replace consonants with digits as follows (after the first letter):
  * b, f, p, v → 1
  * c, g, j, k, q, s, x, z → 2
  * d, t → 3
  * l → 4
  * m, n → 5
  * r → 6
3. If two or more letters with the same number are adjacent in the original 
name (before step 1), only retain the first letter; also two letters with the 
same number separated by 'h' or 'w' are coded as a single number, whereas such 
letters separated by a vowel are coded twice. This rule also applies to the 
first letter.
4. If you have too few letters in your word that you can't assign three numbers,
append with zeros until there are three numbers. If you have more than 3 
letters, just retain the first 3 numbers. Using this algorithm, both "Robert" 
and "Rupert" return the same string "R163" while "Rubin" yields "R150".
"Ashcraft" and "Ashcroft" both yield "A261" and not "A226" (the chars 's' and 
'c' in the name would receive a single number of 2 and not 22 since an 'h' lies 
in between them). "Tymczak" yields "T522" not "T520" (the chars 'z' and 'k' in 
the name are coded as 2 twice since a vowel lies in between them). "Pfister" 
yields "P236" not "P123" (the first two letters have the same number and are 
coded once as 'P'), and "Honeyman" yields "H555"."""


def get_soundex(word):
    """Get the soundex code for the string"""

    word = word.upper()
    letters = [char for char in word if char.isalpha()]

    # Remove all occurrences of H, W.
    letters_to_remove = ('H', 'W')

    # If query contains only 1 letter, return query+"000"
    if len(word) == 1:
        return word + "000"

    first_letter = letters[0]
    letters = letters[1:]

    letters = [char for char in letters if char not in letters_to_remove]
    if len(letters) == 0:
        return first_letter + "000"

    # Replace all consonants with digits according to rules
    letters_to_replace = {('B', 'F', 'P', 'V'): 1, ('C', 'G', 'J', 'K', 'Q',
                                                    'S', 'X', 'Z'): 2,
                          ('D', 'T'): 3, ('L'): 4, ('M', 'N'): 5, ('R'): 6,
                          ('A', 'E', 'I', 'O', 'U', 'Y', 'H', 'W'): 0}

    first_letter = [value if first_letter else first_letter for group, value in
                    letters_to_replace.items()
                    if first_letter in group]
    letters = [value if char else char
               for char in letters
               for group, value in letters_to_replace.items()
               if char in group]

    # Replace all adjacent same digits with one digit.
    letters = [number for index, number in enumerate(letters)
               if (index == len(letters) - 1 or (
                index + 1 < len(letters) and number != letters[index + 1]))]

    if first_letter[0] == letters[0]:
        letters[0] = 0
    else:
        letters.insert(0, word[0])

    first_letter = word[0]
    letters = letters[1:]

    # Remove all 0 from it.
    letters = [number for number in letters if number != 0]

    # Remove all except 3 digits after it.
    letters = [char for char in letters if isinstance(char, int)][0:3]

    # Append 3 zeros if result contains less than 3 digits.
    while len(letters) < 3:
        letters.append(0)

    letters.insert(0, first_letter)
    string = "".join([str(l) for l in letters])

    return string


print(get_soundex('Ashcraft'))
