def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0: 
        return False
    else:
        s = str(s)
        slist = s.split(' ')
        s = '#'
        for word in range(0, len(slist)):
            slist[word] = slist[word].capitalize()
            s += slist[word]
        return s
        
        
print(generate_hashtag("Hello my friends"))