def word_count(f_contents):
    count = 0
    words = f_contents.split()
    for word in words:
        count += 1
    return count

def character_count(f_contents):
    chars = {}
    for character in f_contents:
        if character.lower() in chars:
            chars[character.lower()] += 1
        else:
            chars[character.lower()] = 1
    return chars

def sorted_list_of_dicts(char_dict):
    dict_list = []
    for char in char_dict:
        dict_list.append({"char": char, "num": char_dict[char]}) 
    dict_list.sort(reverse=True, key=sort_on)  
    return dict_list

def sort_on(dict):
    return dict["num"]  