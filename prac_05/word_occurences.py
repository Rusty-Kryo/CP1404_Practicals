"""
- Program to count the occurrences of words in a string.
- Asks for a string, prints the counts of how many each
word in the string.
- this program is case-insensitive

estimate: 1hr
actual: 1hr  4mins

"""



def main():
    # get input string, convert to list
    string = input("Enter Text\n>>>")
    words = string.split()
    # get longest word length
    longest_length = find_long_word(words)
    words_to_count = {}  # pre-allocate
    # from the slides
    for word in words:
        word = word.lower()
        if word in words_to_count:
            words_to_count[word] += 1
        else:
            words_to_count[word] = 1

    # print results
    words_to_count = sorted(words_to_count.items())
    for word, count in words_to_count:
        print(f"{word:{longest_length}} = {count}")

#function to find the longest word length with in the string
def find_long_word(words):
    word_length = []
    for word in words:
        length = len(word)
        word_length.append(length)

    longest_length = max(word_length)

    return longest_length



main()
