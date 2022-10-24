"""
This program computes the piglatin for a word
"""
def pig_latin(word):
    """
    This function loops through the vowels for a vowel, and ife
    initial word is a vowel, it returns word appended with 'way'
    It also loops through the vowel again, if first word is not a vowel
    (Then it's automatically a consonant) so it returns from second item to
    the last item of a word, the first item and also 'ay' concatenated
    """
    vowels = ['a','e','i','o','u']
    for i in vowels:
        if word[0] == i:
            return word + 'way'
        return word[1:] + word[0] + 'ay'
print("Enter a new word: ")
new_word = input()
print(f"The pig latin for the word {new_word} is: {pig_latin(new_word)}")
