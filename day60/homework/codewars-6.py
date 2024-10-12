def pig_latin(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    
    def convert_word(word):
        if word[0] in vowels:
            return word + 'ay'
        else:
          
            for i, char in enumerate(word):
                if char in vowels:
                    
                    return word[i:] + word[:i] + 'ay'
            
            return word + 'ay'
    
    pig_latin_words = [convert_word(word) for word in words]
    
    return ' '.join(pig_latin_words)
