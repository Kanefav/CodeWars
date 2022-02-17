def is_palindrome(s):
    inverted_word = ''
    for each in range(len(s)-1, -1, -1):
        inverted_word += f'{s[each]}'
    if inverted_word.upper() == s.upper(): return True
    return False
        

print(is_palindrome('Abba'))