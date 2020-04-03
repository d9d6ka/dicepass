import argparse
from random import SystemRandom


# Parse arguments
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('filename',
                    nargs='?',
                    type=str,
                    default='',
                    help='Name of wordlist')
parser.add_argument('-d', '--dices',
                    nargs='?',
                    type=int,
                    default=5,
                    help='Number of dices',
                    dest='n_dices')
parser.add_argument('-dm', '--dicemax',
                    nargs='?',
                    type=int,
                    default=6,
                    help='Max number on dice',
                    dest='dice_max')
parser.add_argument('-w', '--words',
                    nargs='?',
                    default=5,
                    type=int,
                    help='Number of words',
                    dest='n_words')
parser.add_argument('-l', '--leet',
                    nargs='?',
                    default='',
                    type=str,
                    help='Leet rules file',
                    dest='leetfile')
parser.add_argument('-lp', '--leetpercent',
                    nargs='?',
                    default=50,
                    type=int,
                    help='Probability of each letter leeting',
                    dest='leetprob')
parser.add_argument('-u', '--upper',
                    action='store_true',
                    dest='upper',
                    help='Random letters to uppercase. It prevails over leeting')
parser.add_argument('-up', '--upperpercent',
                    nargs='?',
                    default=50,
                    type=int,
                    help='Probability of turning letter to uppercase',
                    dest='upperprob')
parser.add_argument('-s', '--sep',
                    nargs='?',
                    default=' ',
                    type=str,
                    help='Words separator',
                    dest='sep')
parser.add_argument('-q', '--quiet',
                    action='store_true',
                    dest='quiet',
                    help='Suppress verbose')
parser.add_argument('-c', '--clip',
                    action='store_true',
                    dest='clip',
                    help='Copy to clipboard')
args = parser.parse_args()

# System cryptogenerator
cryptogen = SystemRandom()

# Import pyperclip
if args.clip:
    import pyperclip

# Correct leetprob
if args.leetprob:
    if args.leetprob > 100:
        args.leetprob = 100
    elif args.leetprob < 0:
        args.leetprob = 0

# Correct upperprob
if args.upperprob:
    if args.upperprob > 100:
        args.upperprob = 100
    elif args.upperprob < 0:
        args.upperprob = 0

# Correct max dice number
if args.dice_max:
    if args.dice_max > 9:
        args.dice_max = 9
    elif args.dice_max < 2:
        print('1 sided dice has no sence!')
        exit(1)


def cryptokey(dices=args.n_dices, dicemax=args.dice_max):
    result = ''
    for i in range(dices):
        tmp_int = cryptogen.randint(1, dicemax)
        result += str(tmp_int)
    return result


def upperword(word, prob=args.upperprob):
    result = ''
    for letter in word:
        if cryptogen.randint(0, 100) <= prob:
            result += letter.upper()
        else:
            result += letter
    return result


def leetword(word, leet, prob=args.leetprob):
    result = ''
    for letter in word:
        if (letter in leet) and (cryptogen.randint(0, 100) <= prob):
            result += cryptogen.choice(leet[letter])
        else:
            result += letter
    return result


def passphrase(dictionary, words=args.n_words, dices=args.n_dices, dicemax=args.dice_max, leet={}, leetprob=args.leetprob, sep=args.sep, upper=args.upper, upperprob=args.upperprob):
    wordlist = [dictionary[cryptokey()] for _ in range(words)]
    if upper:
        wordlist = [upperword(x) for x in wordlist]
    if leet:
        wordlist = [leetword(x, leet) for x in wordlist]
    return sep.join(wordlist)


if __name__ == '__main__':
    if not args.filename:
        print('Wordlist is needed!')
        exit(1)
    wordlist = {}
    leetdict = {}
    with open(args.filename, 'r', encoding='utf8') as eff_large_wordlist:
        for line in eff_large_wordlist:
            splitted_line = line.strip().split('\t')
            wordlist[splitted_line[0]] = splitted_line[1]
    if args.leetfile:
        with open(args.leetfile, 'r', encoding='utf8') as leet_file:
            for line in leet_file:
                splitted_line = line.strip().split('\t')
                if splitted_line[0] not in leetdict:
                    leetdict[splitted_line[0]] = [splitted_line[1]]
                else:
                    leetdict[splitted_line[0]].append(splitted_line[1])
    result = passphrase(wordlist, leet=leetdict)
    if not args.quiet:
        print(result)
    if args.clip:
        pyperclip.copy(result)
