# wrap.py

def wrap(string, max_width):
    cur_len = 0
    text = ""
    while cur_len < len(string):
        text += string[cur_len:max_width + cur_len] + "\n"
        cur_len += max_width
    return text

if __name__ == '__main__':
    string, max_width = "safdsafdsafdsafdsafd", 4
    result = wrap(string, max_width)
    print(result)