def counter_sorted(input_string, reverse = False):
    letters ={}
    input_string = input_string.lower()
    input_string = list(input_string)
    for letter in input_string:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    sorted_letters = list(letters.keys())
    sorted_letters.sort()
    if reverse:
        sorted_dict = {sorted_letters[len(sorted_letters) - (i+1)] : letters.get(sorted_letters[i]) for i in range (len(sorted_letters))}
    else:
        sorted_dict = {sorted_letters[i] : letters.get(sorted_letters[i]) for i in range (len(sorted_letters))}
        
    return sorted_dict
