#Write a script that parse sometext.txt file and outputs:

# Total words in file: 4562
# Total characters: 20123
# Avg words per line: 10.4
# Avg len of word: 8.3

# Note that all stats should exclude punctutation!

'''Something wrong with the encoding of this file.
If you use errors = "ignore" it will remove unnedded characters.'''

'''create function to open the file'''
def open_file(x):
    with open("sometext.txt", encoding = "utf8")as text_file:
        if x == "byline":
            text_line = text_file.readlines()
            return text_line
        else:
            text_file = text_file.read()
            return text_file

'''create function to count all the words(using open_file function as a var)'''
def words_counting(open_file):
    total_words = 0
    #to count the words we have to slip the text in to separated words
    words_list = open_file.split()
    for word in words_list:
        total_words += 1
    return total_words


'''create function to count all the characters'''
def characters_counting(open_file):
    string_file = len(open_file)
    return (f"Total charachters in file: {string_file}")

'''create function to count Avg words per line'''
def avg_words_per_line(open_file, words_counting):
    total_words = words_counting
    number_of_lines = 0
    read_byline = open_file
    for line in read_byline:
        number_of_lines += 1
    words_per_line = total_words / number_of_lines
    return f"Average words per line: {round(words_per_line,1)}"

''' create a function to count Avg len of word:'''
def avg_len_of_word(open_file, words_counting):
    total_words = words_counting
    total_letters = 0
    for letter in open_file:
        if letter.isalpha():
            total_letters += 1
    return f"Total avg len of word: {round (total_letters / total_words,1)}"



print(f"Total words in file: {words_counting(open_file(' '))}")
print(characters_counting(open_file(' ')))
print(avg_words_per_line(open_file('byline'), words_counting(open_file(' '))))
print(avg_len_of_word(open_file(' '), words_counting(open_file(' '))))