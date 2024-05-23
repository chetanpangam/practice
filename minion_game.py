# minion_game.py

# Online Python-3 Compiler (Interpreter)


def minion_game(string):
    # your code goes here
    leg_str = len(string)
    dict_word = 0
    dict_vowel = 0
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    for i,char in enumerate(string):
        if char in vowel_list:
            dict_vowel += (leg_str - i)
        else :
            dict_word += (leg_str - i)

    if dict_word > dict_vowel:
        print("Stuart {}".format(dict_word))
    elif dict_word < dict_vowel:
        print("Kevin {}".format(dict_vowel))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)