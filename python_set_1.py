# 1. Find the largest common divisor of multiple numbers. Define a function with variable number of parameters to
# resolve this.


def largest_common_divisor(a, b):
    if a > b:
        while a > b:
            a = a - b
        return a
    else:
        while b > a:
            b = b - a
        return b


def largest_common_divisor_from_list(*args):
    divisor_list = list(args)
    common = largest_common_divisor(divisor_list[0], divisor_list[1])
    divisor_list = divisor_list[2:]
    for item in divisor_list:
        common = largest_common_divisor(common, item)
    return common


print(">>>>>>>>>>> Largest common divisor from a list <<<<<<<<<<")
print(largest_common_divisor_from_list(24, 20, 12, 20, 20))


# 2. Write a function that calculates how many vowels are in a string.

def is_vowel(char):
    return char in "aeiouAEIOU"


def num_of_vowels(string):
    counter = 0
    for char in string:
        if is_vowel(char):
            counter += 1
    return counter


print(">>>>>>>>>>> Number of vowels in a string <<<<<<<<<<<")
print(num_of_vowels("George"))


# 3. Write a function that returns the number of words that exist in a string. Words are separated by spaces,
# punctuation marks (, ;, ? ! . )

def split_by_given_symbol(string, symbol):
    return string.split(symbol)


def get_num_of_words_in_string(string):
    symbols = ",;?!."
    text = string
    for symbol in symbols:
        text = "".join(split_by_given_symbol(text, symbol))
    text = text.split(" ")
    return len(text)


print(">>>>>>>>>>> Number of words in a string <<<<<<<<<<<")
print(get_num_of_words_in_string("Salut bai, Leo Geo, cmf? Bine; tu!."))


# 4. Write a function that receives two strings as parameters and returns the number of occurrences of the first
# character string in the second.

def occurrences(str1, str2):
    first_char = str1[0]
    counter = 0
    for char in str2:
        if char == first_char:
            counter += 1
    return counter


print(">>>>>>>>>>> Number of occurrences of first char of str1 in str2 <<<<<<<<<<<")
print(occurrences("georgel", "purcel georgggel"))


# 5.Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)

def is_special_character(char):
    if char == '\r' or char == '\t' or char == '\n' or char == '\a' or char == '\b' or char == '\f' or char == '\v':
        return True
    return False


def has_special_characters(string):
    str = string[:]
    for char in str:
        if is_special_character(char):
            return True
    return False


print(">>>>>>>>>>> Does string have special characters? <<<<<<<<<<<")
print(has_special_characters('Georgel purcel\nlala'))


# 6. Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def letter_case(letter):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in lower:
        return 'lower'
    elif letter in upper:
        return 'upper'


def split_into_words(str1):
    words = []
    string = str1 + '_'  # add an _ to simulate the end of the actual string
    string_length = len(string)
    word_index = 0
    i = 0
    while i < string_length - 1:
        if (letter_case(string[i]) == 'lower' and letter_case(string[i + 1]) == 'upper') or (
                letter_case(string[i]) == 'lower' and string[i + 1] == '_'):
            current_word = string[word_index: i + 1]  # get the current word
            words.append(current_word)  # and add it to the list
            word_index = i + 1
        i += 1
    words_length = len(words)
    words[words_length - 1] + string[:-1]  # remove the underscore
    j = 0
    final_words = ''
    while j < words_length:
        final_words = final_words + words[j].lower() + '_'
        j += 1
    final_words = final_words[:-1]
    return final_words


print(">>>>>>>>>>> Transform CamelCase to camel_case <<<<<<<<<<<")
print(split_into_words('UpperCamelCase'))


# 7. Write a function that receives a char_len integer and a variable number of strings (strings) and check that each
# two neighboring strings follow the following rule: the second string starts with the last char_len characters of
# the first string (like the word game pheasant).

def neighbours(char_len, strings):
    i = 0
    strings_length = len(strings)
    print()
    while i < strings_length - 1:
        if strings[i][-char_len:] != strings[i + 1][0: char_len]:
            return False
        i += 1
    return True


print(">>>>>>>>>>> word game pheasant <<<<<<<<<<<")
print(neighbours(3, ['George', 'rge']))

# 8. Give a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float).
# Evaluate the polynomial for the given value. 9. Write a function that returns the largest prime number from a
# string given as a parameter or -1 if the character string contains no prime number. Ex: input:
# 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
