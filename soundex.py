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

    soundex = ""
    soundex += word[0]

    dictionary = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5',
                  'R': '6', 'AEIOUHWY': ''}

    for letter in word[1:]:
        for key in dictionary.keys():
            if letter in key:
                number = dictionary[key]
                if number != soundex[-1]:
                    soundex += number
    soundex = soundex[:4].ljust(4, "0")

    return soundex
