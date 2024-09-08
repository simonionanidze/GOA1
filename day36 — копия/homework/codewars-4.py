def remove_url_anchor(url):
    
    anchor_index = url.find('#')
    
    
    if anchor_index != -1:
        return url[:anchor_index]
    else:
        return url


print(remove_url_anchor("www.codewars.com#about"))  
print(remove_url_anchor("www.codewars.com?page=1")) 
