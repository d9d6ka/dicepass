# dicepass

Easy python script for generating dice passphrases. Finished as far as it does what I've expected from it.

It was written just to feed my paranoia and to practice in Python scripting :)

You should use [passphraseme](https://github.com/micahflee/passphraseme) by @micahflee or any other similar tool on everyday basis.

## Dependencies

Based on Python standard modules. Whether you want autocopy to clipboard work, install [pyperclip](https://pypi.org/project/pyperclip/).

## Usage

You will need the wordlist of the format
```
XXXXX <tab> word
```
where `XXXXX` -- the sequence of dice roll results. `XXXXX` and `word` should be tab delimited.

If you want to use leeting, you will need leet rules tab delimited file of the format
```
letter <tab> replacement
```

Usage:
```
python dicepass.py [-h]
                   [-d [N_DICES]] [-dm [DICE_MAX]]
                   [-w [N_WORDS]]
                   [-l [LEETFILE]] [-lp [LEETPROB]]
                   [-u] [-up [UPPERPROB]]
                   [-s [SEP]] [-q] [-c]
                   [filename]

positional arguments:
  filename              Name of wordlist

optional arguments:
  -h, --help            show this help message and exit
  -d [N_DICES], --dices [N_DICES]
                        Number of dices. Default is 5
  -dm [DICE_MAX], --dicemax [DICE_MAX]
                        Max number on dice. Default is 6
  -w [N_WORDS], --words [N_WORDS]
                        Number of words. Default is 5
  -l [LEETFILE], --leet [LEETFILE]
                        Leet rules file. Default is ''
  -lp [LEETPROB], --leetpercent [LEETPROB]
                        Probability of each letter leeting. Default is 50
  -u, --upper           Random letters to uppercase.
  -up [UPPERPROB], --upperpercent [UPPERPROB]
                        Probability of turning letter to uppercase. Default of 50
  -s [SEP], --sep [SEP]
                        Words separator. Default is ' '
  -q, --quiet           Suppress verbose
  -c, --clip            Copy to clipboard
```

## EFF Large Wordlist

Get it on the [EFF page](https://www.eff.org/ru/deeplinks/2016/07/new-wordlists-random-passphrases).

## Leet rules

Based on [The Slangit Leet Sheet](https://slangit.com/leet_sheet).
