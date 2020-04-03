import sys
from random import SystemRandom


cryptogen = SystemRandom()


def init():
    pass


def cryptoword(list, dices=5, dicemax=6):
    result = ''
    for i in range(dices):
        tmp_int = cryptogen.randrange(dicemax)
        result += str(tmp_int + 1)
    return result


wordlist = {}
with open('eff_large_wordlist.txt', 'r', encoding='utf8') as eff_large_wordlist:
    for line in eff_large_wordlist:
        splitted_line = line.strip().split('\t')
        wordlist[splitted_line[0]] = splitted_line[1]

key = cryptoword(eff_large_wordlist)
print(wordlist[key])
print(wordlist['66666'])
