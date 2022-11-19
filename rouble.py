from sys import argv
from random import choice
from requests import get

def word_list() -> list:
    f = open("/usr/share/rouble/words")
    words = f.read().strip()
    return words.split('\n')

def select_random(words: list) -> str:
    l = len(words)
    return choice(words)

def req(word: str) -> list:
    resp = get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    return resp.json()

def print_word(word: dict) -> None:
    print(f"{word['word']}:")
    for meaning in word['meanings']:
        print(f"    - {meaning['partOfSpeech']}:")
        for d in meaning['definitions']:
            print(f"        - {d['definition']}")

def do_random() -> None:
    resp = None

    while resp is None:
        words = word_list()
        word = select_random(words)
        r = req(word)
        if len(r) == 1:
            resp = r[0]
    

    print_word(resp)


def main() -> None:
    l = len(argv)

    if l > 1:
        for i in range(1, l):
            resp = req(argv[i])
            if len(resp) == 1:
                print_word(resp[0])
    else:
        do_random()

if __name__ == "__main__":
    main()
