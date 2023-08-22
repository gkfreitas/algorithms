def is_palindrome_recursive(word, low_index, high_index):
    print(type(word), len(word))
    if type(word) == str and len(word) == 0:
        return False
    if len(word) == 1 or len(word) == 0:
        return True
    if word[low_index] == word[high_index]:
        listWord = list(word)
        del listWord[high_index]
        del listWord[low_index]
        newHighIndex = len(listWord) - 1
        return is_palindrome_recursive(listWord, low_index, newHighIndex)
    return False
