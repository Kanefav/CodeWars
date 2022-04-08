def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = 0
    for item in range(0, len(vowels)):
        output += sentence.count(vowels[item])
    return output
        

print(get_count('abcdeiou'))