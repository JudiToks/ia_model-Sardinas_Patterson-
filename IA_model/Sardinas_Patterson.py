from itertools import combinations

E = ""
loop_marge = 10

def is_codage(language_list): 
    next = True
    current_lang = set(language_list)
    lang_passed = []
    i = 0
    # print("L"+str(i) +" : "+ str(current_lang))
    while next : 
        current_lang = set(devide(language_list,current_lang)+ devide(current_lang,language_list))
        # print(current_lang)
        # print("L"+str(i+1) +" : "+ str(current_lang))
        if current_lang == None or current_lang == set(): 
            return True

        if E in current_lang and i != 0 : 
            return False
        
        if lang_passed.count(current_lang) > loop_marge : 
            return True
        
        if i > 0 : 
            lang_passed.append(current_lang)
        i += 1
    return True

def devide(language_1,language_2):
    result = []
    temp_residual = ""
    for u in language_1 : 
        for v in language_2:
            temp_residual = get_residual(u,v)
            if temp_residual != v : 
                result.append(temp_residual)
    return result


def get_residual(code , another_code) : 
    return another_code.removeprefix(code)


def generate_combination(lang) : 
    result = []
    for r in range(0, len(lang) ):  
        result.extend(list(combinations(lang, r)))

    return result


def make_code(language) : 
    codable = []
    combinations = generate_combination(language)

    for c in combinations : 
        if(is_codage(list(c))) : 
            codable.append(list(c))

    len_max = max(len(c) for c in codable)
    result = []
    result = [c for c in codable if len(c) == len_max]

    return result