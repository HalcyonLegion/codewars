import re # Module to work with regEx

def disemvowel(str):
    return re.sub(r'[aeiouAEIiOU]', '', str)