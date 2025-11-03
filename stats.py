def get_num_words(s):
    l = s.split()
    return  len(l)

def get_char_count(text):
    text = text.lower()
    ret = {}

    for t in text:
        if t not in ret:
            ret[t] = 1
        else:
            ret[t] += 1
    return ret

def sort_on(items):
    return items["num"]

def report(dic):
    dic.sort(reverse=True, key=sort_on)
    return dic

