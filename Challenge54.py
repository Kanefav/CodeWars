def compress(sentence):
    if sentence == '0': return ''
    output = ''
    map = {}
    sentence = sentence.lower()
    words = sentence.split(' ')
    words_final = sentence.split(' ')
    
    #deleting repeated
    for word in range(len(words)-1, -1, -1):
        if words.count(words[word]) > 1:
            words.pop(word)
            
    #mapping
    for word in range(0, len(words)):
        map[f'{words[word]}'] = word
    
    #enumerating 
    for word in words_final:
        output += f'{map.get(word)}'
    return output
    

print(compress('the one bumble bee one bumble the bee'))