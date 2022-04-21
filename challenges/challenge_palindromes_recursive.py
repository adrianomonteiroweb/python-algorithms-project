def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif len(word) < 2:
        return True
    elif low_index >= high_index:
        if word[low_index] != word[high_index]:
            return False
        else:
            return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
