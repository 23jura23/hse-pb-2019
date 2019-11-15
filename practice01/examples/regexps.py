#!/usr/bin/env python3

import re



def re_examples():
    # email
    simple_email_regex = re.compile("\w+@(\w+\.)+\w+")
    words = re.compile("\w+")
    found = words.match("Hello, Re!")
    regex = re.compile("(\w+)\W+\1$")
    if found:
        print(found.start(), found.end())
    print(words.match("Hello, Re!", endpos=0))
    print(words.match("Hello, Re!", pos=7).span())

    p = re.compile('(a(b)*c)d')
    print("group example")
    print(p.match('abbbcd').group(0))
    print(p.match('acd').group(0, 1, 0))
    print(p.match('abcd').groups())

    p = re.compile(r'(\b\w+)\s+\1')  # boundary, word, whitespace, \1
    print(p.search('Word repeated twice twice').group())
    print(re.sub("not.*good", 'bad', "Homework is not so good, not good!"))
    p = re.compile("not.*?good")
    print(p.sub('bad', "Homework is not so good, not good!",
                count=2))

    p = re.compile('\W+')
    print(p.split('Students, welcome to re world!'))
    print(p.findall('Students, welcome to re world!'))

    russian = re.compile('[а-яА-Я]+')
    print(russian.findall('Привет из России'))

    charref = re.compile("""
 &[#]                # Comment starts with #
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | 0x[0-9a-fA-F]+  # Hexadecimal form
""", re.VERBOSE)
    print(charref.findall("123 012347 0xdeadbeef hello"))
    print(re.search('Vladimir(?! Putin)', 'Vladimir ').group())
    # Real world example IPv4
    # ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
    # (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$

if __name__ == '__main__':
    re_examples()
