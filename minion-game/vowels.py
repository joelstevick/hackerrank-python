vowels = {
    'A': True,
    'E': True,
    'I': True,
    'O': True,
    'U': True
}
stuart = 0
kevin = 0


def is_vowel(string):
    return vowels.get(string[0]) == True


def scan(string):
    global kevin
    global stuart

    freq_stuart = {}
    freq_kevin = {}

    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j]:

                k = 0
                while i + k < len(string) and j + k < len(string):
                    if string[i + k] == string[j + k]:
                        word = string[j:j + k + 1]
                        if len(word.strip()) > 0:
                            if is_vowel(word):
                                stat = freq_kevin.get(word)
                                if stat:
                                    stat["count"] += 1
                                else:
                                    freq_kevin[word] = {
                                        "count": 1,
                                    }
                            else:
                                stat = freq_stuart.get(word)
                                if stat:
                                    stat["count"] += 1
                                else:
                                    freq_stuart[word] = {
                                        "count": 1,
                                    }
                        k += 1
                    else:
                        break
                break
    # score
    for word in freq_stuart.keys():
        stuart += freq_stuart[word]["count"]
    for word in freq_kevin.keys():
        kevin += freq_kevin[word]["count"]


def minion_game(string):
    global stuart
    global kevin

    scan(string)

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif stuart < kevin:
        print(f"Kevin {kevin}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
