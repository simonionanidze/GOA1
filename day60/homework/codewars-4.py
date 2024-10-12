def generate_hashtag(s):
   
    s = s.strip()
    if not s:
        return False
    
    
    words = s.split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    
  
    if len(hashtag) > 140:
        return False
    
    return hashtag
